import aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_admin.app import app as admin_app
from fastapi_admin.providers.login import UsernamePasswordProvider
from tortoise.contrib.fastapi import register_tortoise

from app.api.api import api_router
from app.core.config import settings
from app.core.users import auth_backend, fastapi_users
from app.models import Admin

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_STR)

# FastAPI Admin


@app.on_event("startup")
async def startup() -> None:
    redis = aioredis.from_url(
        "redis://redis:6379",
        decode_responses=True,
        encoding="utf8",
    )
    await admin_app.configure(
        providers=[UsernamePasswordProvider(admin_model=Admin)],
        redis=redis,
    )


app.mount("/admin", admin_app)


# FastAPI Users routes
app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/api/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(), prefix="/api/auth", tags=["auth"]
)
app.include_router(
    fastapi_users.get_users_router(), prefix="/api/users", tags=["users"]
)

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
