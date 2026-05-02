from fastapi import HTTPException
from sqlmodel import Session, select
from core.auth import verify_password
from models.user import User


def login_service(session: Session, username: str, password: str):
    user = session.exec(select(User).where(User.username == username)).first()

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None
    return user