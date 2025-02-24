from tortoise import Tortoise


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


async def close_db():
    await Tortoise.close_connections()
