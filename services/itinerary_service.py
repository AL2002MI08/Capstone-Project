from schemas.itinerary import DayEntry
from sqlmodel import select
from schemas.itinerary import ItineraryResponse
from models.trip import Trip
from models.itinerary import Itinerary
from fastapi import HTTPException
from sqlmodel import Session
from core.config import settings
from anthropic import Anthropic
import json
from core.prompts import system_prompt, prompt

client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

def add_user_message(messages, text):
    user_message = {"role": "user", "content": text}
    messages.append(user_message)
    return messages

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})
    return messages

def generate_itinerary(session: Session, trip_id: int):
    trip = session.get(Trip, trip_id)
    if not trip:
        raise HTTPException(status_code=404, detail="Trip not found")
    itinerary_message = prompt.format(
        destination=trip.destination,
        days=trip.days,
        budget=trip.budget,
        travel_style=trip.trip_style
    )
    
    message = add_user_message([], itinerary_message)
    prefilled_message = add_assistant_message(message, "[")
    
    output = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2000,
        messages=prefilled_message,
        system=system_prompt,
        temperature=0.6
    )
    raw = "[" + output.content[0].text
    itinerary = json.loads(raw)
    db_itinerary = Itinerary(
        trip_id=trip.id,
        days=itinerary,
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

