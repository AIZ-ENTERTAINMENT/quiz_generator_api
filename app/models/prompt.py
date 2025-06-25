from sqlalchemy import JSON, Column, Integer, Text

from app.models.base import BaseORM


class PromptORM(BaseORM):
    __tablename__ = "prompt"
    prompt_id = Column(Integer, primary_key=True)
    prompt_name = Column(Text)
    prompt_content = Column(Text)
    
class OutputFormatORM(BaseORM):
    __tablename__ = "output_format"
    output_format_id = Column(Integer, primary_key=True)
    output_format_name = Column(Text)
    output_format_schema = Column(JSON)