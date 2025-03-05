from invoke import task  # type: ignore

COMPOSE = "docker compose"
EXEC_UV = f"{COMPOSE} exec back uv run"


@task(aliases=["b"])
def build(c):
    c.run(f"{COMPOSE} build")

@task(aliases=["u"])
def up(c):
    c.run(f"{COMPOSE} up -d")


@task(aliases=["s"])
def stop(c):
    c.run(f"{COMPOSE} stop")


@task(aliases=["d"])
def down(c):
    c.run(f"{COMPOSE} down -v")


@task(aliases=["m"])
def migrate(c):
    c.run(f"{EXEC_UV} alembic upgrade head")


@task(aliases=["mm"])
def make_migrations(c):
    c.run(f"{EXEC_UV} alembic revision --autogenerate")


@task(aliases=["bs"])
def back_shell(c):
    c.run(f"{COMPOSE} exec back sh")
