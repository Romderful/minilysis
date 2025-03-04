"""FastAPI entry point."""

from admins.user import UserAdmin
from database import engine
from fastapi import FastAPI
from pydantic import BaseModel
from routes.user import include_user_routes
from sqladmin import Admin

app = FastAPI()
admin = Admin(app, engine)

include_user_routes(app)
admin.add_view(UserAdmin)


class StatusResponse(BaseModel):
    running: str


@app.get("/", tags=["healthcheck"])
async def read_root() -> StatusResponse:
    """Backend api satus."""
    return {"running": "live"}
