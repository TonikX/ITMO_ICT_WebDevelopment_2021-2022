from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator


class Hotel(models.Model):
    """
    Модель отеля
    """

    name = fields.CharField(max_length=255, unique=True, index=True)
    address = fields.CharField(max_length=1023, null=True)
    img_src = fields.CharField(max_length=2047, null=True)
    description = fields.TextField(null=True)
    rating = fields.FloatField(null=True)
    cost_from = fields.FloatField(null=True)


HotelSchema = pydantic_model_creator(Hotel)
