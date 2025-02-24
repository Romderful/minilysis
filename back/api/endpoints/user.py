
from fastapi import APIRouter

from models.user import User


router = APIRouter()


@router.get("/users/")
async def get_users():
    all_users = await User.all()
    return [
        {"id": user.id, "username": user.username, "email": user.email}
        for user in all_users
    ]
