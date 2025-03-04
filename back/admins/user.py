"""User admin."""

from models.user import User
from sqladmin import ModelView


class UserAdmin(ModelView, model=User):
    """User admin."""

    column_list = [User.id, User.name, User.email, User.is_superuser]
