from app.libs.response import SuccessResponse
from app.route import get_router
from app.route.topic_history import service
from app.route.topic_history.schema import TopicHistoryRequest

router = get_router("topic_history")

@router.post("/")
async def create_topic_history(req: TopicHistoryRequest):
    res = await service.create_topic_history(req)
    return SuccessResponse(data=res)

@router.get("/{topic_history_id}")
async def get_topic_history(topic_history_id: int):
    res = await service.get_topic_history(topic_history_id)
    return SuccessResponse(data=res)

@router.put("/{topic_history_id}")
async def update_topic_history(topic_history_id: int, req: TopicHistoryRequest):
    await service.update_topic_history(topic_history_id, req)
    return SuccessResponse(message="Topic history updated")

@router.delete("/{topic_history_id}")
async def delete_topic_history(topic_history_id: int):
    await service.delete_topic_history(topic_history_id)
    return SuccessResponse(message="Topic history deleted")