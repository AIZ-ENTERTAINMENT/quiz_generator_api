"""
models classes for sqlalchemy orm
"""

from app.libs.database import engine
from app.models.prompt import PromptORM
from app.models.quiz_set import QuizSetORM
from app.models.topic_history import TopicHistoryORM
from app.models.user import UserORM


async def setup_engine():
    """create table with engine setup"""
    async with engine.begin() as conn:
        await conn.run_sync(UserORM.metadata.create_all)
        await conn.run_sync(PromptORM.metadata.create_all)
        await conn.run_sync(QuizSetORM.metadata.create_all)
        await conn.run_sync(TopicHistoryORM.metadata.create_all)
        
async def destroy_engine():
    if engine:
        await engine.dispose()
