from invoke import task  # type: ignore

UV_EXEC = "docker compose exec back uv run"


@task
def migrate(c):
    c.run(f"{UV_EXEC} alembic upgrade head")


@task(aliases=["mm"])
def make_migrations(c):
    c.run(f"{UV_EXEC} alembic revision --autogenerate")
