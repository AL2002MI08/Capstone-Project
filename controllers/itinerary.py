from core.db import get_session
from fastapi import Depends
from services import itinerary_service
from fastapi import APIRouter
from core.deps import get_current_user
from sqlmodel import Session
router = APIRouter(prefix="/itinerary", tags=["Itinerary"])

@router.post("/{trip_id}")
def create_itinerary(trip_id: int,session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return itinerary_service.generate_itinerary(session, trip_id)

@router.get("/{trip_id}")
def get_itinerary(trip_id: int,session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return itinerary_service.get_itinerary(session, trip_id)


