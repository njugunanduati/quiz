from datetime import datetime
from sqlalchemy import create_engine
from .config import Config
from sqlalchemy.orm import sessionmaker
from .models import User, Question, Score

engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def get_questions():
    the_questions = session.query(Question).all()
    questions = []
    for row in the_questions:
        questions.append({
            "id": row.id,
            "question": row.question,
            "options": {
                "A": row.option_a,
                "B": row.option_b,
                "C": row.option_c,
                "D": row.option_d
            },
            "correct": row.correct,
            "explanation": row.explanation,
            "points": row.points
        })
    return questions


def check_user(email):
    the_user = session.query(User).filter_by(email=email).first()
    if the_user:
        return the_user.id
    return False

def save_user(first_name, last_name, email):
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email
    )
    session.add(new_user)
    session.commit()
    return session.query(User).filter_by(email=email).first().id

def save_score(user_id, score, total):
    new_score = Score(
        user_id=user_id,
        score=score,
        total=total,
        quiz_date=datetime.now()
    )
    session.add(new_score)
    session.commit()