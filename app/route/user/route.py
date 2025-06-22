from os import environ
from typing import Annotated

import jwt
from fastapi import BackgroundTasks, Depends

from app.libs.jwt import (ALGORITHM, SECRET_KEY, get_admin_user,
                          get_current_user)
from app.libs.response import SuccessResponse
from app.models.user import UserORM
from app.route import get_router
from app.route.user import service
from app.route.user.schema import (CreateUserRequest, LoginUserRequest,
                                   UpdateUserInfoRequest)

router = get_router("user")


@router.post("/signup")
async def create_user(req: CreateUserRequest) -> SuccessResponse:
    decoded_token: dict = jwt.decode(req.token, SECRET_KEY, algorithms=[ALGORITHM])
    user = await service.create_user(
        name=req.name,
        email=decoded_token["email"],
    )
    token = await service.get_access_token(user.email)
    return SuccessResponse(
        data={
            "token": token.access_token,
        }
    )


@router.post("/login")
async def get_google_login_url(email: LoginUserRequest) -> SuccessResponse:
    user = await service.login_user(email)
    return SuccessResponse(data=user)


@router.post("/login/kakao")
async def get_kakao_login_token(
    token: LoginUserRequest, bg_task: BackgroundTasks
) -> SuccessResponse:
    user = await service.kakao_login_token(token, bg_task)
    return SuccessResponse(data=user)


@router.put("/")
async def update_user(
    update_request: UpdateUserInfoRequest,
    user: Annotated[UserORM, Depends(get_current_user)],
) -> SuccessResponse:
    """
    User 정보 업데이트
    """
    await service.update_user(user, update_request)
    return SuccessResponse(message="Successfully updated user information")


@router.delete("/")
async def delete_user(
    user: Annotated[UserORM, Depends(get_current_user)],
) -> SuccessResponse:
    await service.delete_user(user)
    return SuccessResponse(message="Successfully deleted user information")


@router.get("/admin")
async def get_user_token(
    user_email, user: Annotated[UserORM, Depends(get_admin_user)]
) -> SuccessResponse:
    res = await service.get_access_token(user_email)
    return SuccessResponse(data=res)


if environ.get("DEPLOY_PHASE", "dev") == "local":

    @router.get("/local")
    async def get_local_user() -> SuccessResponse:
        res = await service.fake_login()
        return SuccessResponse(data=res)
