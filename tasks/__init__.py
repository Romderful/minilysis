from invoke import task  # type: ignore


@task
def migrate(c):
    c.run("docker compose exec back uv run alembic upgrade head")


@task(aliases=["mm"])
def make_migrations(c):
    c.run("docker compose exec back uv run alembic revision --autogenerate")
