import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class Survey(Base):
    __tablename__ = 'smartwork'

    id = Column(Integer, primary_key=True)
    ratings = Column(Integer, nullable=False)
    comments = Column(String(250), nullable=True)
    date = Column(DateTime, default=func.now())
    team_id = Column(Integer, nullable=True)


engine = create_engine('sqlite:///smartwork.sqlite')

Base.metadata.create_all(engine)
