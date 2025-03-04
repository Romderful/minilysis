from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class StatusResponse(BaseModel):
    running: str


@app.get("/")
async def read_root() -> StatusResponse:
    return {"running": "live"}
