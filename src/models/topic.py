from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Topic(Base):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True)
    name = Column(String)
