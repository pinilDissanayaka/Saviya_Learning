from database.database import localSession, engine, Base
from models.user import UserModel
from utils.hash import generateHash, verifyHash
from schema.user import User
from fastapi import HTTPException

Base.metadata.create_all(engine)

session=localSession()

def createUser(user:User)->bool:
    user=user.model_dump()
    
    existingUser=session.query(UserModel).filter_by(email=user['email']).first()
    
    if existingUser:
        return False
    else:
        password=generateHash(rowPassword=user['password'])
        user.pop('password')
        user['password']=password
        newUser=UserModel(**user)
        session.add(newUser)
        session.commit()
        session.refresh(newUser)
        
        return True