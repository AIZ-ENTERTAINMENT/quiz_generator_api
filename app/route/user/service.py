import os
import ssl
import time
from datetime import timedelta

import certifi
from fastapi import HTTPException, status

from app.libs.async_http_client import AsyncHTTPClient
from app.libs.database import with_session
from app.libs.jwt import ACCESS_TOKEN_EXPIRE_HOURS, Token, create_access_token
from app.libs.logger_config import logger
from app.libs.response import ErrorResponse
from app.models.user import UserORM
from app.route.user.schema import (KakaoUserInfoResponse, LoginUserRequest,
                                   UpdateUserInfoRequest)

# certifi 인증서 파일을 사용하여 SSL 컨텍스트 생성
ssl_context = ssl.create_default_context(cafile=certifi.where())


def is_valid_google_token(aud):
    return (
        os.environ.get("GOOGLE_CLIENT_ID") == aud
        or os.environ.get("GOOGLE_CLIENT_ANDROID_ID") == aud
        or os.environ.get("GOOGLE_CLIENT_IOS_ID") == aud
    )


async def get_kakao_info(kakao_token: str) -> KakaoUserInfoResponse:
    """
    카카오 사용자 정보 가져오기 (Kakao API를 호출하여 사용자 정보를 반환)
    """
    headers = {"Authorization": f"Bearer {kakao_token}"}

    kakao_client = AsyncHTTPClient("kapi.kakao.com", 443, header=headers)
    try:
        if os.environ.get("DEPLOY_PHASE", "local") != "local":
            res = await kakao_client.get(suffix="/v2/user/me")
        else:
            res = await kakao_client.get(suffix="/v2/user/me", ssl=ssl_context)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to fetch Kakao user info")

    if not res and "id" in res:
        raise HTTPException(400, "Invalid token")

    kakao_account = res.get("kakao_account", {})
    email = kakao_account.get("email")
    profile = kakao_account.get("profile", {})
    profile_image = profile.get("profile_image_url", "")
    name = profile.get("nickname", "")
    thumbnail_image = profile.get("thumbnail_image_url", "")

    if not email:
        raise HTTPException(
            status_code=400, detail="Email not provided in Kakao account info"
        )

    return KakaoUserInfoResponse(
        email=email,
        name=name,
        profile_image=profile_image,
        thumbnail_image=thumbnail_image,
    )


@with_session
async def delete_user(user: UserORM, session=None):
    try:
        user = await UserORM.get(user_id=user.user_id, session=session)
        await user.delete(session=session)
    except Exception as e:
        logger.error(f"Failed to delete user: {e}")
        raise HTTPException(
            400, detail=ErrorResponse(error=f"Invalid request", code="400").model_dump()
        )


@with_session
async def kakao_login_token(token: LoginUserRequest, bg_task, session=None):
    """
    카카오 토큰으로 로그인 토큰 발급.
    """
    kakao_token = token.token
    kakao_info: KakaoUserInfoResponse = await get_kakao_info(kakao_token)

    logger.info(f"Kakao user info: {kakao_info}")
    email = kakao_info.email
    name = kakao_info.name if kakao_info.name else "user"
    profile_image = kakao_info.profile_image if kakao_info.profile_image else None
    thumbnail_image = kakao_info.thumbnail_image if kakao_info.thumbnail_image else None
    try:
        user = await UserORM.get(email=email, session=session)
        if not user:
            user = await create_user(
                email=email,
                name=name,
                profile_image=profile_image,
                thumbnail_image=thumbnail_image,
                session=session,
                bg_task=bg_task,
            )
        token = await get_access_token(user.email, expires=False, session=session)
        user_id = await get_access_token(
            user.email,
            expires=False,  ## 만료 안되게.
            session=session,
        )
        return {
            "name": user.name,
            "token": token.access_token,
            "user_id": user_id.access_token,
            "profile_image": user.profile_image,
            "thumbnail_image": user.thumbnail_image,
        }
    except:
        raise HTTPException(
            400, detail=ErrorResponse(error="Invalid request", code="400").model_dump()
        )


@with_session
async def login_user(req: LoginUserRequest, session=None):
    """
    User 로그인
    """
    google_client = AsyncHTTPClient("https://oauth2.googleapis.com", 443)
    res = await google_client.get(suffix="tokeninfo", params={"id_token": req.token})
    if not res or not is_valid_google_token(res["aud"]):
        raise HTTPException(
            400, detail=ErrorResponse(error="Invalid request", code="400").model_dump()
        )
    if int(res["exp"]) < int(time.time()):
        raise HTTPException(
            400, detail=ErrorResponse(error="Token Expired", code="400").model_dump()
        )
    email = res["email"]
    user_name = "user"
    try:
        user = await UserORM.get(email=email, session=session)
        if not user:
            access_token = create_access_token(data={"email": email})
            token = Token(access_token=access_token, token_type="bearer")
        else:
            token = await get_access_token(user.email, expires=False, session=session)
        return {
            "name": user.name if user else user_name,
            "token": token.access_token,
            "user_id": token.access_token if user else None,
        }
    except Exception as e:
        logger.error(f"Failed to login user: {e}")
        raise HTTPException(
            400, detail=ErrorResponse(error="Invalid request", code="400").model_dump()
        )


@with_session
async def fake_login(session=None):
    token = await get_access_token("qw", session=session)
    user_id = await get_access_token("qw", expires=False, session=session)

    return {
        "name": "er",
        "token": token.access_token,
        "user_id": user_id.access_token,
    }


@with_session
async def update_user(
    user: UserORM, update_request: UpdateUserInfoRequest, session=None
):
    """
    User 정보 업데이트
    """
    try:
        # 세션이 달라서 다시 가져와야함
        usr = await UserORM.get(user_id=user.user_id, session=session)
        await usr.update_by_dict(update_request.model_dump(), session=session)

    except Exception as e:
        raise HTTPException(
            400, detail=ErrorResponse(error="Invalid request", code="400").model_dump()
        )


@with_session
async def create_user(session=None, **kwargs) -> UserORM:
    """
    Create User
    """
    try:
        user = await UserORM.create(session=session, commit=False, flush=True, **kwargs)
        user_id = user.__dict__["user_id"]
        
        await session.commit()
        user = await UserORM.get(user_id=user_id, session=session)
        return user
    except:
        raise Exception("Failed to create user")


@with_session
async def get_user_by_email(email: str, session=None):
    """
    Get User by email
    """
    user = await UserORM.get(email=email, session=session)
    return user


@with_session
async def get_access_token(user_email: str, expires=False, session=None):
    # app 으로 가면서 expires=False로 바뀜
    user = await get_user_by_email(user_email, session=session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    if expires:
        access_token = create_access_token(
            data={"email": user.email, "user_id": user.user_id},
            expires_delta=access_token_expires,
        )
    else:
        access_token = create_access_token(
            data={"email": user.email, "user_id": user.user_id}
        )
    return Token(access_token=access_token, token_type="bearer")




@with_session
async def update_onboarding_status(user_id: int, session=None):
    """
    Update onboarding status
    """
    user = await UserORM.get(user_id=user_id, session=session)
    await user.update_by_dict({"onboarding": False}, session=session)
    return {"message": "Success"}
