from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: Optional[str] = "čtenář"

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int
    role: str

    class Config:
        from_attributes = True
