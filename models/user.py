from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(min_length=5, max_length=100, nullable=False)
    hashed_password: str = Field(min_length=5, nullable=False)