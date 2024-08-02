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
        return 409
    else:
        password=generateHash(rowPassword=user['password'])
        user.pop('password')
        user['password']=password
        newUser=UserModel(**user)
        session.add(newUser)
        session.commit()
        session.refresh(newUser)
        
        return 201
    
def getUserByUserName(userName:str, rowPassword):
    existingUser=session.query(UserModel).filter(UserModel.user_name==userName).first()
    if existingUser:
        isTrue=verifyHash(rowPassword=rowPassword, hashedPassword=existingUser.password)
        if isTrue:
            return 200
        else:
            return 400
    else:
        return 401