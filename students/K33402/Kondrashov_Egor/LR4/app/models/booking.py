from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Booking(models.Model):
    """
    Модель бронирования отеля пользователем
    """

    user = fields.ForeignKeyField("models.User", related_name="bookings")
    hotel = fields.ForeignKeyField("models.Hotel", related_name="bookings")
    starts_at = fields.DateField()
    ends_at = fields.DateField()
    number_of_guests = fields.SmallIntField()


BookingSchema = pydantic_model_creator(Booking)
