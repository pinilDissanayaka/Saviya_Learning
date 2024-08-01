from typing import Optional, List
from enum import Enum
from uuid import UUID, uuid4
from pydantic import BaseModel


class Gender(str. Enum):
    male="male"
    female="female"
    
class Role(str, Enum):
    admin="admin"
    user="user"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    gender: Gender
    role= Role