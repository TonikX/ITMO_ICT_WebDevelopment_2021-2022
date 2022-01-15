from datetime import date

from fastapi_users import models
from fastapi_users.db import TortoiseBaseUserModel
from tortoise import fields
from tortoise.contrib.pydantic import PydanticModel

from app.models.booking import Booking


class UserSchema(models.BaseUser):
    """
    Base Pydantic user model
    """

    first_name: str | None
    middle_name: str | None
    last_name: str | None
    birthdate: date | None

    class Config:
        schema_extra = {
            "example": {
                "id": "cc41bca5-ae42-464e-8a5f-b0009dc01f95",
                "email": "test@test.com",
                "is_active": True,
                "is_superuser": False,
                "is_verified": False,
                "first_name": "Тест",
                "middle_name": "Тестович",
                "last_name": "Тестов",
                "birthdate": "1990-05-01",
            }
        }


class UserCreate(models.BaseUserCreate):
    """
    Pydantic model for user creation
    """

    class Config:
        schema_extra = {
            "example": {"email": "test@test.com", "password": "TESTtest123"}
        }


class UserUpdate(models.BaseUserUpdate):
    """
    Pydantic model for updating user info
    """

    first_name: str | None
    middle_name: str | None
    last_name: str | None
    birthdate: date | None

    class Config:
        schema_extra = {
            "example": {
                "email": "test@test.com",
                "password": "TESTtest123",
                "first_name": "Тест",
                "middle_name": "Тестович",
                "last_name": "Тестов",
                "birthdate": "1990-05-01",
            }
        }


class User(TortoiseBaseUserModel):
    """
    Tortoise user model (fields stored in DB)
    """

    first_name = fields.CharField(max_length=255, null=True)
    middle_name = fields.CharField(max_length=255, null=True)
    last_name = fields.CharField(max_length=255, null=True)
    birthdate = fields.DateField(null=True)

    bookings: fields.ReverseRelation[Booking]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class UserDB(UserSchema, models.BaseUserDB, PydanticModel):
    """
    Pydantic model that maps DB User fields
    (for example, it has hashed_password)
    """

    class Config:
        orm_mode = True
        orig_model = User
