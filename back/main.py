from contextlib import asynccontextmanager
from fastapi import FastAPI

from db.session import close_db, init_db
from api.endpoints.user import router as user_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)


@app.get("/")
async def read_root():
    return {"running": "live"}
