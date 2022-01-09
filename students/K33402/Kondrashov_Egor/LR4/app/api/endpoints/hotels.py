from typing import Any

from fastapi import APIRouter

from app.models import Hotel, HotelSchema

router = APIRouter()


@router.get("", response_model=list[HotelSchema])  # type: ignore
async def get_hotels() -> Any:
    return await HotelSchema.from_queryset(Hotel.all())
