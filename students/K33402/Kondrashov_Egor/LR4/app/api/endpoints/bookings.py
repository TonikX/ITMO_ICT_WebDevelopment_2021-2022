from typing import Any

from fastapi import APIRouter, Depends

from app.core.users import current_user
from app.models import BookingSchema, UserDB

router = APIRouter()


@router.get("", response_model=list[BookingSchema])  # type: ignore
async def get_users_bookings(user: UserDB = Depends(current_user)) -> Any:
    """
    Список броней текущего пользователя
    """
    return user.bookings
