"""
models classes for sqlalchemy orm
"""

from app.libs.database import engine

from .user import *


async def setup_engine():
    """create table with engine setup"""
    async with engine.begin() as conn:
        await conn.run_sync(UserORM.metadata.create_all)
        
async def destroy_engine():
    if engine:
        await engine.dispose()
