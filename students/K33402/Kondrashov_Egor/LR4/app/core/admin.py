"""
Кастомизация админки FastAPI Admin
https://fastapi-admin.github.io/reference/resource/
"""
from fastapi_admin.app import app
from fastapi_admin.resources import Model

from app.models import Hotel


@app.register
class HotelResource(Model):
    label = "Hotel"
    model = Hotel
    fields = ["id", "name"]
