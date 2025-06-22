from fastapi import HTTPException

from app.libs.database import with_session
from app.models.topic_history import TopicHistoryORM
from app.route.topic_history.schema import TopicHistoryRequest


@with_session
async def create_topic_history(req: TopicHistoryRequest, session=None):
    "Create Topic History"
    try :
        return await TopicHistoryORM.create(
            topic=req.topic,
            sub_topic=req.sub_topic,
            related_topic=req.related_topic,
            session=session,
        )
    except :
        raise HTTPException(status_code=422, detail="Failed to create topic history")

@with_session
async def get_topic_history(topic_history_id: int, session=None):
    "Get Topic History"
    try :
        return await TopicHistoryORM.get(topic_history_id=topic_history_id, session=session)
    except :
        raise HTTPException(status_code=422, detail="Failed to get topic history")

@with_session
async def update_topic_history(topic_history_id: int, req: TopicHistoryRequest, session=None):
    "Update Topic History"
    topic_history = await TopicHistoryORM.get(topic_history_id=topic_history_id, session=session)
    if not topic_history:
        raise HTTPException(status_code=404, detail="Topic history not found")
    await topic_history.update_by_dict(
        data=req.model_dump(),
        session=session,
    )

@with_session
async def delete_topic_history(topic_history_id: int, session=None):
    "Delete Topic History"
    topic_history = await TopicHistoryORM.get(topic_history_id=topic_history_id, session=session)
    if not topic_history:
        raise HTTPException(status_code=404, detail="Topic history not found")
    await topic_history.delete(session=session)