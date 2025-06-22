from sqlalchemy import JSON, Column, Integer, String

from app.models.base import BaseORM


class TopicHistoryORM(BaseORM):
    __tablename__ = "topic_history"
    topic_history_id = Column(Integer, primary_key=True)
    topic = Column(String)
    sub_topic = Column(JSON)
    related_topic = Column(JSON)