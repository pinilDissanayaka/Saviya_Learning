from fastapi import FastAPI, HTTPException, status
from schema.userSchema import User
from models.userModel import UserModel
from database.database import localSession
from utils.hash import generateHash, verifyHash

app=FastAPI()

session=localSession()

@app.post("/register", tags=['u'])
async def register(user:User):
    user=user.model_dump()
    
    existingUser=session.query(UserModel).filter_by(email=user['email']).first()
    
    if existingUser:
        raise HTTPException(400, detail="Email already registered")
    else:
        password=generateHash(rowPassword=user['password'])
        user.pop('password')
        user['password']=password
        newUser=UserModel(**user)
        session.add(newUser)
        session.commit()
        session.refresh(newUser)
        
        return {"detail":"user created successfully"}
        
        
          
@app.get("/login", tags=['g'])
async def addResource(user_name:str, password:str):
    existingUser=session.query(UserModel).filter(UserModel.user_name==user_name).first()
    
    if existingUser:
        isTrue=verifyHash(rowPassword=password, hashedPassword=existingUser.password)
        if isTrue:
            return {"detail":"user logging successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail="Bad request")
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect email")