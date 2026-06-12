from fastapi import FastAPI
from contextlib import asynccontextmanager
from controllers import user_routes, auth, trip, itinerary
from models import User, Trip, Itinerary

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(user_routes.router, prefix="/users")
app.include_router(trip.router)
app.include_router(itinerary.router)

