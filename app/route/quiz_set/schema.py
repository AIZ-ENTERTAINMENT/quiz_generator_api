from pydantic import BaseModel


class QuizSetRequest(BaseModel):
    main_topic: str
    quiz_topic: str
    difficulty: str
    cost: int
    