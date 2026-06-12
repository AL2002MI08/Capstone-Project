from sqlmodel import SQLModel, Field

class TripBase(SQLModel):
    destination: str 
    days: int = Field(ge=1)
    budget: int = Field(ge=1)
    trip_style: str


class TripCreate(TripBase):
    pass

class TripResponse(TripBase):
    message: str | None = None

class TripUpdate(SQLModel):
    destination: str | None = None
    days: int | None = Field(default=None, ge=1)
    budget: int | None = Field(default=None, ge=0)
    trip_style: str | None = None