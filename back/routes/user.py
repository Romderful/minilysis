"""User routes."""

from database import get_async_session
from domains.auth import auth_backend, fastapi_users
from fastapi import APIRouter, Depends, FastAPI
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from models.user import User, UserCreate, UserRead, UserUpdate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

users_router = APIRouter(prefix="/users")


@users_router.get(path="", tags=["users"])
async def get_users(db: AsyncSession = Depends(get_async_session)) -> Page[UserRead]:
    """Get all users."""
    return await paginate(db, select(User))


def include_auth_routes(app: FastAPI):
    """Include all user-related routers in the app."""
    routes = [
        (fastapi_users.get_auth_router, "/auth/jwt", ["auth"], auth_backend),
        (fastapi_users.get_register_router, "/auth", ["auth"], UserRead, UserCreate),
        (fastapi_users.get_reset_password_router, "/auth", ["auth"]),
        (fastapi_users.get_verify_router, "/auth", ["auth"], UserRead),
        (fastapi_users.get_users_router, "/users", ["users"], UserRead, UserUpdate),
    ]

    for router_func, prefix, tags, *args in routes:
        app.include_router(router_func(*args), prefix=prefix, tags=tags)
