from typing import Any

from pydantic import BaseModel, model_serializer


class UpdateUserInfoRequest(BaseModel):
    name: str

    @model_serializer
    def ser(self) -> dict[str, Any]:
        return {"name": self.name.strip()}


class LoginUserRequest(BaseModel):
    token: str


class KakaoUserInfoResponse(BaseModel):
    email: str
    name: str
    profile_image: str
    thumbnail_image: str


class CreateUserRequest(BaseModel):
    name: str
    token: str
