from app.libs.response import SuccessResponse
from app.route import get_router
from app.route.quiz_set import service
from app.route.quiz_set.schema import QuizSetRequest

router = get_router("quiz_set")

@router.post("/")
async def create_quiz_set(req: QuizSetRequest):
    res = await service.create_quiz_set(req)
    return SuccessResponse(data=res)

@router.get("/{quiz_set_id}")
async def get_quiz_set(quiz_set_id: int):
    res = await service.get_quiz_set(quiz_set_id)
    return SuccessResponse(data=res)

@router.put("/{quiz_set_id}")
async def update_quiz_set(quiz_set_id: int, req: QuizSetRequest):
    await service.update_quiz_set(quiz_set_id, req)
    return SuccessResponse(message="Quiz set updated")

@router.delete("/{quiz_set_id}")
async def delete_quiz_set(quiz_set_id: int):
    await service.delete_quiz_set(quiz_set_id)
    return SuccessResponse(message="Quiz set deleted")