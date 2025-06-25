from app.libs.response import SuccessResponse
from app.route import get_router
from app.route.topic import service
from app.route.topic.schema import TopicHistoryRequest

router = get_router("topic")

@router.get("/google_trend")
async def get_google_trend():
    # Get Google Trend
    res = await service.get_google_trend()
    return SuccessResponse(data=res)

#challenger 퀴즈 생성
@router.post("/challenger/topic_curation")
async def create_topic_curation(topic : str):
    res = await service.create_challenger_topic(topic)
    return SuccessResponse(data=res)

#beginner 퀴즈 생성
@router.post("/beginner/topic_curation")
async def create_topic_curation(topic : str):
    res = await service.create_beginner_topic(topic)
    return SuccessResponse(data=res)

@router.post("/topic_history")
async def create_topic_history(req: TopicHistoryRequest):
    res = await service.create_topic_history(req)
    return SuccessResponse(data=res)

@router.get("/topic_history/{topic_history_id}")
async def get_topic_history(topic_history_id: int):
    res = await service.get_topic_history(topic_history_id)
    return SuccessResponse(data=res)

@router.put("/topic_history/{topic_history_id}")
async def update_topic_history(topic_history_id: int, req: TopicHistoryRequest):
    await service.update_topic_history(topic_history_id, req)
    return SuccessResponse(message="Topic history updated")

@router.delete("/topic_history/{topic_history_id}")
async def delete_topic_history(topic_history_id: int):
    await service.delete_topic_history(topic_history_id)
    return SuccessResponse(message="Topic history deleted")