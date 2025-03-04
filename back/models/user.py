"""User model."""

import uuid

from fastapi_users import schemas
from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from models.base import Base
from sqlalchemy import Column, String


class User(SQLAlchemyBaseUserTableUUID, Base):
    """User model."""

    name = Column(String, nullable=True)


class UserRead(schemas.BaseUser[uuid.UUID]):
    """User read schema."""


class UserCreate(schemas.BaseUserCreate):
    """User create schema."""


class UserUpdate(schemas.BaseUserUpdate):
    """User update schema."""
