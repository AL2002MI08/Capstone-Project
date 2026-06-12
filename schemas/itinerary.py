from pydantic import BaseModel, field_validator
from typing import List

class DayEntry(BaseModel):
    day: int
    activities: List[str]
    @field_validator("day")
    @classmethod
    def validate_day(cls, day: int) -> int:
        if day < 1:
            raise ValueError("Day must be at least 1")
        return day

class ItineraryBase(BaseModel):
    trip_id: int
    days: List[DayEntry]

class ItineraryCreate(ItineraryBase):
    pass

class ItineraryResponse(ItineraryBase):
    days: List[DayEntry]
    message: str

