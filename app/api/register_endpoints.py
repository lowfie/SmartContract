from fastapi import FastAPI

from app.api.healthcheck.route import healthcheck
from app.api.tokens.route import tokens
from app.settings.config import API_NAME, API_VERSION

app = FastAPI(
    title=API_NAME,
    version=API_VERSION
)

app.include_router(healthcheck, tags=["healthcheck"])
app.include_router(tokens, tags=["tokens"])
