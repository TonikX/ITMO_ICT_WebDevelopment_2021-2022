from typing import Any

from fastapi import APIRouter, Depends

from app.core.users import current_user
from app.models import Booking, BookingDBSchema, BookingInSchema, UserDB

router = APIRouter()


@router.get("", response_model=list[BookingDBSchema])
async def get_users_bookings(user: UserDB = Depends(current_user)) -> Any:
    """
    Список броней текущего пользователя
    """
    return user.bookings


@router.post("", response_model=BookingDBSchema)
async def create_booking(
    booking: BookingInSchema, user: UserDB = Depends(current_user)
) -> Any:
    """
    Создание бронирования авторизированным пользователем
    """
    booking.user_id = user.id
    booking_obj = await Booking.create(**booking.dict(exclude_unset=True))
    return await BookingDBSchema.from_tortoise_orm(booking_obj)
