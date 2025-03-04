"""FastAPI entry point."""

from database import engine
from fastapi import FastAPI
from models.user import User
from pydantic import BaseModel
from routes.user import include_user_routes
from sqladmin import Admin, ModelView

app = FastAPI()
include_user_routes(app)
admin = Admin(app, engine)


class StatusResponse(BaseModel):
    running: str


@app.get("/", tags=["healthcheck"])
async def read_root() -> StatusResponse:
    """Backend api satus."""
    return {"running": "live"}


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.name, User.email, User.is_superuser]


admin.add_view(UserAdmin)
