from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True, nullable=False)


class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    question = Column(String)
    option_a = Column(String)
    option_b = Column(String)
    option_c = Column(String) 
    option_d = Column(String) 
    correct = Column(String)
    explanation = Column(String)
    points = Column(Integer)


class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    score = Column(Integer)
    total = Column(Integer)
    quiz_date = Column(DateTime)


