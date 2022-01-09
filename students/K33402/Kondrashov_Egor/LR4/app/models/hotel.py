from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Hotel(models.Model):
    name = fields.CharField(max_length=255, unique=True, index=True)


HotelSchema = pydantic_model_creator(Hotel)
