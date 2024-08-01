from database import Base
from sqlalchemy import Column, Integer, String


class UserModel(Base):
    __tablename__='user'
    
    id=Column(Integer, primary_key=True)
    user_name=Column(String(20))
    email=Column(String(20))
    

    
    