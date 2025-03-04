"""User routes."""

from domains.auth import auth_backend, fastapi_users
from fastapi import FastAPI
from models.user import UserCreate, UserRead, UserUpdate


def include_user_routes(app: FastAPI):
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
