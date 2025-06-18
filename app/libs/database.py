from functools import wraps
from typing import AsyncIterable, Optional

from sqlalchemy.engine import Engine
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import Session, scoped_session

from app.libs.logger_config import logger
from app.libs.serializer import json_dumps

__all__ = ["with_session", "engine", "configure_sqlalchemy"]

engine: Optional[Engine] = None
SessionMaker: Optional[scoped_session] = None


def configure_sqlalchemy(
    connection_uri: str,
    engine_options: Optional[dict] = None,
):
    """Configure SQLAlchemy engine and scoped session."""
    global engine, SessionMaker

    if engine:
        return

    options = {
        "echo": False,
        "json_serializer": lambda data: json_dumps(data, indent=None),
    }
    if engine_options:
        options.update(engine_options)
    engine = create_async_engine(connection_uri, **engine_options or {})
    SessionMaker = async_sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False,
    )


async def get_db_session() -> AsyncIterable[Session]:
    session = SessionMaker()
    try:
        yield session
        await session.commit()
    except Exception as err:
        logger.error(
            f"{__name__} - Error - " + "Failed to get_db_session", exc_info=err
        )
        await session.rollback()
        raise err
    finally:
        await session.close()


def with_session(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        if "session" in kwargs:
            return await func(*args, **kwargs)
        async for session in get_db_session():
            return await func(*args, session=session, **kwargs)

    return wrapper
