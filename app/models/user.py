from sqlalchemy import Boolean, Column, Integer, String

from app.models.base import BaseORM


class UserORM(BaseORM):
    """
    User ORM

    Args:
        BaseORM (_type_): _description_
    """

    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), nullable=False, unique=True, index=True)
    name = Column(String(50), nullable=False)
    is_admin = Column(Boolean, nullable=False, default=False)
