from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(min_length=1, max_length=50, nullable=False)
    hashed_password: str = Field(min_length=1, max_length=50, nullable=False)