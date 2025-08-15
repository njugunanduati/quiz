import os
from typing import Union
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from auth_bearer import JWTBearer
from functools import wraps
from utils import create_access_token,create_refresh_token,verify_password,get_hashed_password
from sqlalchemy.orm import Session
import schemas
from models import User, TokenTable, Question
from database import Base, engine, SessionLocal
from utils import get_hashed_password
# from pydantic import BaseModel
# import psycopg2
# import json
# from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
# import database files

load_dotenv()


# Database connection function
# def get_db_connection():
#     conn = psycopg2.connect(
#         host=os.getenv('DB_HOST'),
#         database=os.getenv('DB_DATABASE'),
#         user=os.getenv('DB_USERNAME'),
#         password=os.getenv('DB_PASSWORD')
#     )
#     return conn

Base.metadata.create_all(engine)
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()


@app.get('/api/v1/')
def home():
    return {'message': 'Welcome to the Python Quiz API'}

@app.get('/api/v1/users')
def getusers( dependencies=Depends(JWTBearer()),session: Session = Depends(get_session)):
    user = session.query(User).all()
    return user

@app.post("/api/v1/auth/signup")
def sign_up(user: schemas.UserCreate, session: Session = Depends(get_session)):
    existing_user = session.query(User).filter_by(email=user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    encrypted_password = get_hashed_password(user.password)

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name, 
        email=user.email, 
        password=encrypted_password
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message":"user created successfully"}

@app.post('/api/v1/auth/signin')
def sign_in(request: schemas.requestdetails, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    
    access=create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = TokenTable(user_id=user.id,  access_token=access,  refresh_token=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {
        "access_token": access,
        "refresh_token": refresh,
    }


@app.post('/api/v1/auth/changepassword')
def change_password(request: schemas.changepassword, db: Session = Depends(get_session)):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    
    if not verify_password(request.old_password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid old password")
    
    encrypted_password = get_hashed_password(request.new_password)
    user.password = encrypted_password
    db.commit()
    
    return {"message": "Password changed successfully"}


@app.get('/api/v1/questions')
def get_questions(dependencies=Depends(JWTBearer()), session: Session = Depends(get_session)):
    # Fetch questions from the database
    # Return them in a paginated format
    questions = session.query(Question).all()
    return questions

# @app.post('/api/v1/question')
# def add_question(question: Question) -> Union[dict, str]:
#     question = question.model_dump()
#     print('question', question)
#     # Add a new question to the database
#     # conn = get_db_connection()
#     # cur = conn.cursor()
#     # query = """
#     #     INSERT INTO questions (question, options, correct, explanation, points)
#     #     VALUES (%s, %s, %s, %s, %s)
#     #     RETURNING id
#     # """
#     # print('==', json.dumps(question.options))
#     # cur.execute(query, (question.question, question.options, question.correct, question.explanation, question.points))
#     # conn.commit()
#     # question_id = cur.fetchone()['id']
#     # conn.close()
#     the_question = Question(
#         question=question['question'],
#         options=question['options'],
#         correct=question['correct'],
#         explanation=question['explanation'],
#         points=question['points']
#     )
#     created_question = QuestionCreate(the_question)
#     return {'message': f'Question added successfully with id: {created_question.id}'}