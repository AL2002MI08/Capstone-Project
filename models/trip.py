from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List


class Trip(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    destination: str
    days: int
    budget: int
    trip_style: str
    user_id: int = Field(foreign_key="user.id")
    itineraries: List["Itinerary"] = Relationship(back_populates="trip")