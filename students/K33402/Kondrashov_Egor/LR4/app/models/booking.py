from datetime import date
from uuid import UUID

from tortoise import fields, models
from tortoise.contrib.pydantic import PydanticModel


class Booking(models.Model):
    """
    Модель бронирования отеля пользователем
    """

    user = fields.ForeignKeyField("models.User", related_name="bookings")
    hotel = fields.ForeignKeyField("models.Hotel", related_name="bookings")
    starts_at = fields.DateField()
    ends_at = fields.DateField()
    number_of_guests = fields.SmallIntField()


class BookingInSchema(PydanticModel):
    hotel_id: int
    starts_at: date
    ends_at: date
    number_of_guests: int
    user_id: UUID | None

    class Config:
        orm_mode = True
        orig_model = Booking
        schema_extra = {
            "example": {
                "hotel_id": 1,
                "starts_at": "2022-01-12",
                "ends_at": "2022-01-13",
                "number_of_guests": 2,
            }
        }


class BookingDBSchema(BookingInSchema):
    id: int | None
