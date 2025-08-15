from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# import database config file
from config import Config

# create a postgres engine instance
engine = create_engine(Config.DATABASE_URL)

# Create declarative base meta instance
Base = declarative_base()

# Create session local class for local session
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False) 