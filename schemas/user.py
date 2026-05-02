from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str

class UserUpdate(UserCreate):
    hashed_password: str