from sqlalchemy import Column, Integer, String

from app.models.base import BaseORM


class QuizSetORM(BaseORM):
    __tablename__ = "quiz_set"
    quiz_set_id = Column(Integer, primary_key=True)
    main_topic = Column(String)
    quiz_topic = Column(String)
    difficulty = Column(String)
    cost = Column(Integer)