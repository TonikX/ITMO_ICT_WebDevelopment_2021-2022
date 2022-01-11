from typing import Any

from fastapi import APIRouter
from tortoise.contrib.fastapi import HTTPNotFoundError

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


@router.get(
    "/{hotel_id}",
    response_model=HotelSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def get_hotel(hotel_id: int) -> Any:
    """
    Retrieve hotel by id
    """
    return await HotelSchema.from_queryset_single(Hotel.get(id=hotel_id))
