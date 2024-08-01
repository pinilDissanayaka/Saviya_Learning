from fastapi import FastAPI, HTTPException
from schema import User
from models import UserModel
from database import localSession


app=FastAPI()

session=localSession()

@app.post("/register")
async def register(user:User):
    user=user.model_dump()
    
    existingUser=session.query(UserModel).filter_by(email=user['email']).first()
    
    if existingUser:
        raise HTTPException(400, detail="Email already registered")
    else:
        newUser=UserModel(**user)
        session.add(newUser)
        session.commit()
        session.refresh(newUser)
        
@app.post("/add-resources/{user_id}")
async def addResource(user_id: int):
    pass
    


    
    
    
    

    
    