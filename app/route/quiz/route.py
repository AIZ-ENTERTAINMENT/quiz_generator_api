from app.libs.response import SuccessResponse
from app.route import get_router
from app.route.quiz import service

router = get_router("quiz")


@router.post("/beginner/create_quiz")
async def create_beginner_quiz(begginer_sub_topic : str):
    res = await service.create_beginner_quiz(begginer_sub_topic)
    return SuccessResponse(data=res)