from datetime import datetime, timedelta, timezone

import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
from pydantic import BaseModel

from app.libs.database import with_session
from app.models.user import UserORM

SECRET_KEY = "56df5be05bb3decb78d1db2230ae02b8caefb50e3267c293e4d26f11463fb793"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24


class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
        to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)


def get_api_key(api_key_header: str = Security(api_key_header)):
    return api_key_header


@with_session
async def get_user(email: str, id: int, session=None) -> UserORM:
    return await UserORM.get(email=email, user_id=id, session=session)


async def get_current_user(token: str = Security(get_api_key)) -> UserORM:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("user_id"))
        email: str = payload.get("email")
        if not email:
            raise credentials_exception
        if not user_id:
            raise credentials_exception
        user = await get_user(email, user_id)
        if not user:
            raise credentials_exception
    except jwt.InvalidTokenError as e:
        raise credentials_exception
    return user

async def get_current_user_optional(
    token: str = Security(get_api_key),
) -> UserORM | None:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = int(payload.get("user_id"))
        email: str = payload.get("email")
        if not email:
            return None
        if not user_id:
            return None
        user = await get_user(email, user_id)
        if not user:
            return None
    except jwt.InvalidTokenError:
        return None
    return user


async def get_admin_user(token: str = Security(get_api_key)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    user = await get_current_user(token)
    if not user.is_admin:
        raise credentials_exception
    return user
