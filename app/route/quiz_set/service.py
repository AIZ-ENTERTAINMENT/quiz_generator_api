from fastapi import HTTPException

from app.libs.database import with_session
from app.models.quiz_set import QuizSetORM
from app.route.quiz_set.schema import QuizSetRequest


@with_session
async def create_quiz_set(req: QuizSetRequest, session=None):
    "Create Quiz Set"
    try :
        return await QuizSetORM.create(
            main_topic=req.main_topic,
            quiz_topic=req.quiz_topic,
            difficulty=req.difficulty,
            cost=req.cost,
            session=session,
        )
    except :
        raise HTTPException(status_code=422, detail="Failed to create quiz set")

@with_session
async def get_quiz_set(quiz_set_id: int, session=None):
    "Get Quiz Set"
    quiz_set = await QuizSetORM.get(quiz_set_id=quiz_set_id, session=session)
    if not quiz_set:
        raise HTTPException(status_code=404, detail="Quiz set not found")
    return quiz_set

@with_session
async def update_quiz_set(quiz_set_id: int, req: QuizSetRequest, session=None):
    "Update Quiz Set"
    quiz_set = await QuizSetORM.get(quiz_set_id=quiz_set_id, session=session)
    if not quiz_set:
        raise HTTPException(status_code=404, detail="Quiz set not found")
    await quiz_set.update_by_dict(
        data=req.model_dump(),
        session=session,
    )

@with_session
async def delete_quiz_set(quiz_set_id: int, session=None):
    "Delete Quiz Set"
    #Terry : 퀴즈 셋 삭제시 dynamo에서 퀴즈들도 삭제 필요
    quiz_set = await QuizSetORM.get(quiz_set_id=quiz_set_id, session=session)
    if not quiz_set:
        raise HTTPException(status_code=404, detail="Quiz set not found")
    await quiz_set.delete(session=session)