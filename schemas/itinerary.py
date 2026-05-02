from pydantic import BaseModel
from typing import List


class Itinerary(BaseModel):
    trip_id: int
    days: List