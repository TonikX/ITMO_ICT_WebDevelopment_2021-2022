from pathlib import Path

from pydantic import BaseSettings

ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent


class Settings(BaseSettings):
    API_STR = "/api"
    SECRET_KEY = "PBKFUClGw8wgp5IxgxGEHohN4BV24DX2"
    PROJECT_NAME = "Bookings"
    DATABASE_URL = "postgres://postgres:rzttfSFdrBrJku1Q@db/bookings"

    class Config:
        case_sensitive = True


settings = Settings()


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URL},
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}
