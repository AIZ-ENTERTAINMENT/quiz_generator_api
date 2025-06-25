from pydantic import BaseModel


class TopicHistoryRequest(BaseModel):
    topic : str
    sub_topic : list[str]
    related_topic : list[str]
    difficulty : str