import services.itinerary_service
from core.deps import get_current_user
from sqlmodel import Session
from schemas.itinerary import ItineraryCreate
from fastapi import APIRouter, Depends
from core.db import get_session
from services import itinerary_service


router = APIRouter(prefix="/itinerary", tags=["Itinerary"])

@router.post("")
def create_itinerary(itinerary: ItineraryCreate,session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return itinerary_service.create_itinerary(session, itinerary)

@router.get("/{trip_id}")
def get_itinerary(trip_id: int,session: Session = Depends(get_session), user: str = Depends(get_current_user)):
    return itinerary_service.get_itinerary(session, trip_id)


