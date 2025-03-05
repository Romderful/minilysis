"""FastAPI entry point."""

from admins.user import UserAdmin
from database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from routes.user import include_user_routes
from sqladmin import Admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

include_user_routes(app)

admin = Admin(app, engine)
admin.add_view(UserAdmin)


class StatusResponse(BaseModel):
    status: str


@app.get("/", tags=["healthcheck"])
async def read_root() -> StatusResponse:
    """Backend api satus."""
    return {"status": "live"}
