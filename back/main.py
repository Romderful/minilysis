"""FastAPI entry point."""

from admins.user import UserAdmin
from database import engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from pydantic import BaseModel
from routes.user import include_auth_routes, users_router
from sqladmin import Admin

app = FastAPI()

add_pagination(app)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

include_auth_routes(app)
app.include_router(users_router)

admin = Admin(app, engine)
admin.add_view(UserAdmin)


class StatusResponse(BaseModel):
    status: str


@app.get("/", tags=["healthcheck"])
async def read_root() -> StatusResponse:
    """Backend api satus."""
    return {"status": "live"}
