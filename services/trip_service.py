from schemas.trips import TripCreate, Trip, TripResponse
from sqlmodel import Session
from fastapi import Depends
from core.db import get_session


def create_trip(trip: TripCreate, session: Session = Depends(get_session)):
    db_trip = Trip.model_validate(trip)
    session.add(db_trip)
    session.commit()
    session.refresh(db_trip)
    return TripResponse(
        id=db_trip.id,
        destination=db_trip.destination,
        days=db_trip.days,
        budget=db_trip.budget,
        trip_style=db_trip.trip_style,
        message="Trip created successfully"
    )