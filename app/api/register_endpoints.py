from fastapi import FastAPI

from app.api.healthcheck.healthcheck import healthcheck
from app.settings.config import API_NAME, API_VERSION

app = FastAPI(
    title=API_NAME,
    version=API_VERSION
)

app.include_router(healthcheck, tags=["healthcheck"])
