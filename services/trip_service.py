from annotated_types import T
from schemas.trips import TripCreate, TripResponse, TripUpdate
from fastapi import HTTPException
from models.trip import Trip
from sqlmodel import Session, select
from fastapi import Depends
from core.db import get_session
import time


def get_user_trips(session: Session, user_id: int):
    return session.exec(select(Trip).where(Trip.user_id == user_id)).all()

def get_trip(session: Session, trip_id: int):
    trip = session.get(Trip, trip_id)

    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found.")
    return trip

def create_trip(user_id: int, trip: TripCreate, session: Session = Depends(get_session)):
    db_trip = Trip.model_validate(trip, update={"user_id": user_id})
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

def update_trip(trip_id: int, session: Session, trip: TripUpdate):
    db_trip = session.get(Trip, trip_id)
    if not db_trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    db_trip.destination = trip.destination
    db_trip.days = trip.days
    db_trip.budget = trip.budget
    db_trip.trip_style = trip.trip_style
    session.add(db_trip)
    session.commit()
    session.refresh(db_trip)
    return TripResponse(
        id=db_trip.id,
        destination=db_trip.destination,
        days=db_trip.days,
        budget=db_trip.budget,
        trip_style=db_trip.trip_style,
        message="Trip updated successfully"
    )

def delete_trip(session: Session, trip_id: int):
    db_trip = session.get(Trip, trip_id)
    if not db_trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    session.delete(db_trip)
    session.commit()
    session.refresh(db_trip)
    return TripResponse(
        id=db_trip.id,
        destination=db_trip.destination,
        days=db_trip.days,
        budget=db_trip.budget,
        trip_style=db_trip.trip_style,
        message="Trip deleted successfully"
    )


def confirm_booking(destination: str):
    time.sleep(3)
    return f"Hello your trip to {destination} has been booked successfully"