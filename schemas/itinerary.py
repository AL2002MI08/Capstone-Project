from pydantic import BaseModel
from typing import List


class ItineraryBase(BaseModel):
    trip_id: int
    days: List[dict]

class ItineraryCreate(ItineraryBase):
    pass

class ItineraryResponse(ItineraryBase):
    message: str

