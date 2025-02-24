from tortoise import Tortoise

from models.user import User


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://postgres:postgres@db:5432/minilysisdb",
    },
    "apps": {
        "models": {
            "models": ["models.user", "aerich.models"],
            "default_connection": "default",
        },
    },
}


async def init_db():
    await Tortoise.init(config=TORTOISE_ORM)
    await User.create(username="admin", email="admin@mail.com")
    await User.create(username="Mika", email="mika@mail.com")
    await User.create(username="Romain", email="romain@mail.com")


async def close_db():
    await Tortoise.close_connections()
