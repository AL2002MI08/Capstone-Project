from fastapi import FastAPI
from contextlib import asynccontextmanager
from core.db import init_db
from controllers import user_routes, auth

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(user_routes.router, prefix="/users")
