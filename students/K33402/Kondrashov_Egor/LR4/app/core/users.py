"""
Настройки для FastAPI Users
https://fastapi-users.github.io/fastapi-users/configuration/full-example/#tortoise-orm
"""
from typing import Any

from fastapi import Depends
from fastapi_users import BaseUserManager, FastAPIUsers
from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    JWTStrategy,
)
from fastapi_users.db import TortoiseUserDatabase

from app.core.config import settings
from app.models import User, UserCreate, UserDB, UserSchema, UserUpdate


async def get_user_db() -> Any:
    yield TortoiseUserDatabase(UserDB, User)


class UserManager(BaseUserManager[UserCreate, UserDB]):
    """
    https://fastapi-users.github.io/fastapi-users/configuration/user-manager/
    """

    user_db_model = UserDB
    reset_password_token_secret = settings.SECRET_KEY
    verification_token_secret = settings.SECRET_KEY


async def get_user_manager(user_db: Any = Depends(get_user_db)) -> Any:
    yield UserManager(user_db)


bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=settings.SECRET_KEY, lifetime_seconds=60 * 60 * 24)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    UserSchema,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_user = fastapi_users.current_user()
