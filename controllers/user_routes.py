from typing import List
from fastapi import Depends, APIRouter
from core.deps import get_current_user
from schemas.user import UserCreate, UserResponse
from sqlmodel import Session
from core.db import get_session
from services import user_service

router = APIRouter(tags=["Users"])

@router.get("", response_model=List[UserResponse])
def get_users(session: Session = Depends(get_session)):
    return user_service.get_users(session)

@router.post("", response_model=UserResponse)
def create_user(user: UserCreate, session: Session = Depends(get_session), current_user: str = Depends(get_current_user)):
    return user_service.create_user(session, user.username, user.password)

@router.get("/me")
def read_user(user: str = Depends(get_current_user)):
    return {"current_user": user}

