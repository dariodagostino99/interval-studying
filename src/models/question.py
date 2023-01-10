from sqlalchemy import Column, Integer, String, ForeignKey
from src.models import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    value = Column(String)
