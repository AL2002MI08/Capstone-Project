from sqlmodel import SQLModel, Field

class TripBase(SQLModel):
    destination: str
    days: int
    budget: int
    trip_style: str


class TripCreate(TripBase):
    pass

class TripResponse(TripBase):
    message: str | None = None

class TripUpdate(SQLModel):
    destination: str | None = None
    days: int | None = None
    budget: int | None = None
    trip_style: str | None = None