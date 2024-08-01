from database import Base, localSession, engine
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__='user'
    
    id=Column(Integer, primary_key=True)
    
    