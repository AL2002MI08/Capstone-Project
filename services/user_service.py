from sqlmodel import Session, select
from models.user import User
from fastapi import HTTPException
from core.auth import hash_password


def create_user(session: Session, email, password):
    user_exists = session.exec(select(User).where(User.email == email)).first()

    if user_exists:
        raise HTTPException(status_code=400, detail="User already have an account")
    user = User(
        email=email,
        hashed_password=hash_password(password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session):
    users = session.exec(select(User)).all()
    return users

def get_user(session: Session, email: str):
    user = session.exec(select(User).where(User.email == email)).first()
    return user

def update_user(session: Session, email: str, new_password: str):
    user = session.exec(select(User).where(User.email == email)).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if len(new_password) < 8:
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters")
    user.hashed_password = hash_password(new_password)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def delete_user(session: Session, username: str):
    user = session.exec(select(User).where(User.username == username)).first()
    if not user or user.username != username:
        raise HTTPException(status_code=404, detail="User not found")

    session.delete(user)
    session.commit()
    session.refresh(user)

    return "User deleted successfully!"