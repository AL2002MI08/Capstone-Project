from schemas.itinerary import DayEntry
from sqlmodel import select
from schemas.itinerary import ItineraryResponse
from models.trip import Trip
from models.itinerary import Itinerary
from fastapi import HTTPException
from schemas.itinerary import ItineraryCreate
from sqlmodel import Session




def create_itinerary(session: Session, itinerary: ItineraryCreate):
    trip = session.get(Trip, itinerary.trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    db_itinerary = Itinerary(
        trip_id=itinerary.trip_id,
        days=[day.model_dump() for day in itinerary.days],
    )
    session.add(db_itinerary)
    session.commit()
    session.refresh(db_itinerary)
    
    return ItineraryResponse(
        trip_id=db_itinerary.trip_id,
        days=[DayEntry(**day) for day in db_itinerary.days],
        message="Itinerary created successfully!"
    )

def get_itinerary(session: Session, trip_id: int):
    statement = select(Itinerary).where(Itinerary.trip_id == trip_id)
    item = session.exec(statement).first()
    if not item:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return item

