from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel, EmailStr



class User(BaseModel):
    id: Optional[UUID] = uuid4()
    user_name: str
    email:EmailStr
    
    
class Resource(BaseModel):
    id: Optional[UUID]=uuid4
    user_id: UUID
    