from sqlmodel import SQLModel, Field

class TripBase(SQLModel):
    destination: str
    days: int
    budget: int
    trip_style: str

class Trip(TripBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class TripCreate(TripBase):
    pass

class TripResponse(TripBase):
    message: str

class TripUpdate(SQLModel):
    destination: str | None = None
    days: int | None = None
    budget: int | None = None
    trip_style: str | None = None