from fastapi import FastAPI

from app.api import goals

app = FastAPI()

app.include_router(goals.router, prefix="/api/v1", tags=["goals"])

