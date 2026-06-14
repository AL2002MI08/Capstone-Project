from fastapi import FastAPI
from controllers import user_routes, auth, trip, itinerary

app = FastAPI()
app.include_router(auth.router)
app.include_router(user_routes.router, prefix="/users")
app.include_router(trip.router)
app.include_router(itinerary.router)

