from typing import List, Literal, Optional, Type, TypeVar, Union

from sqlalchemy import Column, DateTime, Select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session, as_declarative

from app.libs.database import with_session
from app.libs.utils import seoul_tz_now_datetime

C = TypeVar("C", bound="BaseORM")


@as_declarative()
class BaseORM:
    """
    Base class for all models.
    Define all db basic actions
    """

    created_at = Column(DateTime, default=seoul_tz_now_datetime)
    updated_at = Column(
        DateTime, default=seoul_tz_now_datetime, onupdate=seoul_tz_now_datetime
    )
    _select = None

    def __init__(self: C, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def create_select(
        cls: Type[C],
        *filters,
        order_by: Optional[Union[Column, List[Column], desc]] = None,
        limit: int = None,
        offset: int = None,
        clear: bool = True,
        skip_locked: bool = False,
        **filter_by,
    ) -> Select:
        select: Select = cls._select or Select(cls)
        if filters:
            select = select.filter(*filters)
        if filter_by:
            select = select.filter_by(**filter_by)
        if order_by is not None:
            if isinstance(order_by, list):
                select = select.order_by(*order_by)
            else:
                select = select.order_by(order_by)
        if limit is not None:
            select = select.limit(limit)
        if offset is not None:
            select = select.offset(offset)
        if skip_locked:
            select = select.with_for_update(skip_locked=True)
        if clear:
            cls._select = None
        return select

    @classmethod
    @with_session
    async def get(
        cls: Type[C],
        *filters,
        skip_locked=False,
        session: Optional[AsyncSession] = None,
        **filter_by,
    ) -> Optional[C]:
        query = cls.create_select(*filters, **filter_by, skip_locked=skip_locked)
        result = await session.execute(query)
        return result.scalars().first()

    @classmethod
    @with_session
    async def list(
        cls: Type[C],
        *filters,
        order_by: Optional[Union[Column, List[Column], desc]] = None,
        limit: int = None,
        offset: int = None,
        session: Optional[Session] = None,
        columns: List[Column] = None,
        distinct: List[Column] = None,
        **filter_by,
    ) -> List[C]:
        query = cls.create_select(
            *filters, order_by=order_by, limit=limit, offset=offset, **filter_by
        )
        results = await session.execute(query)
        return results.scalars().all()

    @classmethod
    @with_session
    async def create(
        cls: Type[C],
        commit: bool = True,
        flush: bool = False,
        session: Optional[AsyncSession] = None,
        merge: bool = False,
        refresh: bool = True,
        **kwargs,
    ) -> C:
        return await cls(**kwargs).save(
            commit=commit, flush=flush, merge=merge, session=session, refresh=refresh
        )

    @with_session
    async def save(
        self,
        commit: bool = True,
        flush: bool = False,
        refresh: bool = True,
        merge: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> C:
        """Save this object on database."""
        if merge:
            await session.merge(self)
        else:
            session.add(self)
        if commit:
            await session.commit()
        if flush:
            await session.flush()
        if (commit or flush) and refresh:
            await session.refresh(self)
        return self

    @with_session
    async def update_by_dict(
        self,
        data: dict,
        commit: Optional[bool] = True,
        session: Optional[Session] = None,
    ) -> C:
        for key, value in data.items():
            setattr(self, key, value)
        await self.save(session=session, commit=commit)

    @with_session
    async def delete(
        self,
        commit: bool = True,
        flush: bool = False,
        session: Optional[AsyncSession] = None,
    ) -> C:
        await session.delete(self)
        if commit:
            await session.commit()
        if flush:
            await session.flush()
        return self

    @classmethod
    @with_session
    async def delete_all(
        cls: Type[C],
        *filters,
        commit: bool = True,
        flush: bool = False,
        session: Optional[Session] = None,
        **filter_by,
    ) -> int:
        select = cls.create_select(*filters, **filter_by)
        result = await session.execute(select)
        items = result.scalars().all()
        count = len(items)
        for item in items:
            await item.delete(session=session)
        if commit:
            await session.commit()
        if flush:
            await session.flush()
        return count

    @classmethod
    async def join(
        cls: Type[C],
        join_type: Literal["inner", "outer"] = "inner",
        *cols,
        **filters,
    ) -> Type[C]:
        select = cls.create_select(clear=False)
        if join_type == "inner":
            select = select.join(*cols)
        elif join_type == "outer":
            select = select.outerjoin(*cols)
        cls._select = select.filter_by(**filters)
        return cls
