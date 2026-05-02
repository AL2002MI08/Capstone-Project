from sqlmodel import Session, select
from models.user import User
from fastapi import HTTPException
from core.auth import hash_password


def create_user(session: Session, username, password):
    user = User(
        username=username,
        hashed_password=hash_password(password)
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def get_users(session: Session):
    users = session.exec(select(User)).all()
    return users

def get_user(session: Session, username: str):
    user = session.exec(select(User).where(User.username == username)).first()
    return user

def update_user(session: Session, username: str, new_password: str):
    user = session.exec(select(User).where(User.username == username)).first()
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