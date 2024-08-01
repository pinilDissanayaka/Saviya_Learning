from fastapi import FastAPI, HTTPException
from schema import User
from models import UserModel
from database import localSession


app=FastAPI()

session=localSession()

@app.post("/register")
async def register(user:User):
    user=user.model_dump()
    session.add(user)
    session.commit()
    
    

    
    