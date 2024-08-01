from fastapi import FastAPI, HTTPException, status
from schema.user import User
from crud.user import createUser
from utils.hash import generateHash, verifyHash

app=FastAPI()


@app.post("/register", tags=['User'])
async def register(user:User):
    status=createUser(user=user)
    if status:
        return {"detail":"user created successfully"}
    else:
        raise HTTPException(400, detail="Email already registered")
        
        
          
@app.get("/login", tags=['User'])
async def addResource(user_name:str, password:str):
    existingUser=True
    
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