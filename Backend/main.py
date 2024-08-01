from fastapi import FastAPI, HTTPException, status
from schema import User
from models import UserModel
from database import localSession
from passlib.hash import pbkdf2_sha512


app=FastAPI()

session=localSession()

@app.post("/register")
async def register(user:User):
    user=user.model_dump()
    
    existingUser=session.query(UserModel).filter_by(email=user['email']).first()
    
    if existingUser:
        raise HTTPException(400, detail="Email already registered")
    else:
        password=pbkdf2_sha512.hash(user['password'])
        user.pop('password')
        user['password']=password
        newUser=UserModel(**user)
        session.add(newUser)
        session.commit()
        session.refresh(newUser)
        
        return {"detail":"user created successfully"}
        
        
          
@app.post("/add-resources/{user_id}")
async def addResource(user_id: int):
    pass
    


    
    
    
    

    
    