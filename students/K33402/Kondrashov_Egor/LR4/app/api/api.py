from fastapi import APIRouter

from app.api.endpoints import hotels

api_router = APIRouter()
api_router.include_router(hotels.router, prefix="/hotels", tags=["Отели"])
