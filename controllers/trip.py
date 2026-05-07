from services import user_service
from core.deps import get_current_user
from schemas.trips import TripResponse
from schemas.trips import TripUpdate
from sqlmodel import Session
from core.db import get_session
from schemas.trips import TripCreate
from fastapi import APIRouter, BackgroundTasks, Depends
from services import trip_service
from typing import List

from services.trip_service import confirm_booking

router = APIRouter(prefix= "/trips", tags=["Trips"])

@router.get("", response_model=List[TripResponse])
def get_all_trips(username: str = Depends(get_current_user), session: Session = Depends(get_session)):
    user = user_service.get_user(session, username)
    return trip_service.get_user_trips(session, user.id)

@router.post("")
def create_trip(trip: TripCreate, background_tasks: BackgroundTasks, user_id: int, session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    new_trip = trip_service.create_trip(user_id, trip, session)
    background_tasks.add_task(confirm_booking(trip.destination))
    return new_trip


@router.get("/{trip_id}")
def get_trip(trip_id: int, session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return trip_service.get_trip(session, trip_id)

@router.patch("/{trip_id}")
def update_trip(trip_id: int, trip: TripUpdate, session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return trip_service.update_trip(trip_id, session, trip)

@router.delete("/{trip_id}")
def delete_trip(trip_id: int, session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return trip_service.delete_trip(session, trip_id)
