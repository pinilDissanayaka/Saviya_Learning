import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')

engine=create_engine(url=DATABASE_URL)

Base=declarative_base()

localSession=sessionmaker(bind=engine, autocommit=False, autoflush=False)