from pydantic import BaseModel
import datetime

class User(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class requestdetails(BaseModel):
    email:str
    password:str
        
class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class changepassword(BaseModel):
    email:str
    old_password:str
    new_password:str

class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime.datetime


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
