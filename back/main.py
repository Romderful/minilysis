"""FastAPI entry point."""

from domains.auth import auth_backend, fastapi_users
from fastapi import FastAPI
from models.user import UserCreate, UserRead, UserUpdate
from pydantic import BaseModel

app = FastAPI()


class StatusResponse(BaseModel):
    running: str


@app.get("/", tags=["healthcheck"])
async def read_root() -> StatusResponse:
    """Backend api satus."""
    return {"running": "live"}


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
