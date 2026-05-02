from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from core.db import get_session
from services.auth import login_service as login_service
from core.auth import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(session: Session = Depends(get_session), form_data: OAuth2PasswordRequestForm = Depends()):
    user = login_service(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": user.username})
    return {
        "access_token": token,
        "token_type": "bearer"
    }