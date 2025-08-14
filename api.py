import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import json
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
load_dotenv()


# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_DATABASE'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn


class Question(BaseModel):
    id: int
    question: str
    options: list
    correct: str
    explanation: str
    points: int

class QuestionCreate(BaseModel):
    question: str
    options: list
    correct: str
    explanation: str
    points: int
    class Config:
        orm_mode = True

class User(BaseModel):
    first_name: str
    last_name: str
    email: str

app = FastAPI()


@app.get('/api/v1/')
def home():
    return {'message': 'Welcome to the Python Quiz API'}

@app.get('/api/v1/questions')
def get_questions():
    # Fetch questions from the database
    # Return them in a paginated format
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM questions")
    rows = cur.fetchall()
    print('rows', rows)
    conn.close()

    questions = []
    for row in rows:
        questions.append(Question(**row))
    return questions

@app.post('/api/v1/question')
def add_question(question: Question) -> Union[dict, str]:
    question = question.model_dump()
    print('question', question)
    # Add a new question to the database
    # conn = get_db_connection()
    # cur = conn.cursor()
    # query = """
    #     INSERT INTO questions (question, options, correct, explanation, points)
    #     VALUES (%s, %s, %s, %s, %s)
    #     RETURNING id
    # """
    # print('==', json.dumps(question.options))
    # cur.execute(query, (question.question, question.options, question.correct, question.explanation, question.points))
    # conn.commit()
    # question_id = cur.fetchone()['id']
    # conn.close()
    the_question = Question(
        question=question['question'],
        options=question['options'],
        correct=question['correct'],
        explanation=question['explanation'],
        points=question['points']
    )
    created_question = QuestionCreate(the_question)
    return {'message': f'Question added successfully with id: {created_question.id}'}