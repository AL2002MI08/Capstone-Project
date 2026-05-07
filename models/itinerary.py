from sqlalchemy import JSON, Column
from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional


class Itinerary(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    trip_id: int = Field(foreign_key="trip.id", ondelete="CASCADE")
    days: List[dict] = Field(sa_column=Column(JSON))
    trip: Optional["Trip"] = Relationship(back_populates="itineraries")
