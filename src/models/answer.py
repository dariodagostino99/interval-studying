from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import Base


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    question_id = Column(Integer, ForeignKey("questions.id"))
    value = Column(String)
