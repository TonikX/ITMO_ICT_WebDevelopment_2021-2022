from typing import Any

from fastapi import APIRouter

from app.models import Hotel, HotelSchema

router = APIRouter()


@router.get("", response_model=list[HotelSchema])  # type: ignore
async def get_hotels(city: str = "") -> Any:
    """
    Список отелей
    """
    queryset = Hotel.all()
    if city:
        queryset = queryset.filter(address__icontains=city)
    return await HotelSchema.from_queryset(queryset)
