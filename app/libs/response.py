from functools import wraps
from typing import Annotated, Any, Dict, Generic, Optional, TypeVar

from pydantic import AfterValidator, BaseModel

from app.models.base import BaseORM

T = TypeVar("T")


def convert_orm_to_dict(data):
    def delete_unused_key(data):
        new_obj = {}
        for key, value in data.__dict__.items():
            if not key.startswith("_"):
                new_obj[key] = value
        return new_obj

    if data and isinstance(data, BaseORM):
        return delete_unused_key(data)
    elif data and type(data) == list:
        return list(
            map(lambda x: delete_unused_key(x) if isinstance(x, BaseORM) else x, data)
        )
    return data


class SuccessResponse(BaseModel, Generic[T]):
    message: Optional[str] = None
    data: Annotated[T | Dict[str, Any] | None, AfterValidator(convert_orm_to_dict)] = (
        None
    )


class ErrorResponse(BaseModel):
    error: str
    code: Optional[str] = None
