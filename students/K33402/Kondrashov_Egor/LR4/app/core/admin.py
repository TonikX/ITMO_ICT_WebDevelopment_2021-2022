"""
Кастомизация админки FastAPI Admin
https://fastapi-admin.github.io/reference/resource/
"""
from fastapi_admin.app import app
from fastapi_admin.resources import Model

from app.models import Hotel, User


@app.register
class HotelResource(Model):
    label = "Hotels"
    model = Hotel


@app.register
class UserResource(Model):
    label = "Users"
    model = User
    fields = ["email", "first_name", "middle_name", "last_name", "birthdate"]
