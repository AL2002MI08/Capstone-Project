from sqlmodel import SQLModel, Field
from typing import Optional


class UserTrip(SQLModel, table=True):
    """Join table for many-to-many relationship between User and Trip"""
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", primary_key=True)
    trip_id: Optional[int] = Field(default=None, foreign_key="trip.id", primary_key=True)
