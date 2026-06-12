from fastapi import HTTPException
from sqlmodel import Session, select
from core.auth import verify_password
from models.user import User


def login_service(session: Session, email: str, password: str):
    user = session.exec(select(User).where(User.email == email)).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email")

    if not verify_password(password, user.hashed_password):
        return None
    return user