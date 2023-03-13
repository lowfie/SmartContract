from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.healthcheck.route import healthcheck
from app.api.tokens.route import tokens
from app.settings.config import (
    USER_POSTGRES,
    PASSWORD_POSTGRES,
    HOST_POSTGRES,
    PORT_POSTGRES,
    DATABASE_POSTGRES,
    API_NAME,
    API_VERSION
)

app = FastAPI(
    title=API_NAME,
    version=API_VERSION
)

url = "asyncpg://{user}:{password}@{host}:{port}/{database}".format(
        user=USER_POSTGRES,
        password=PASSWORD_POSTGRES,
        host=HOST_POSTGRES,
        port=PORT_POSTGRES,
        database=DATABASE_POSTGRES
    )

register_tortoise(
        app,
        db_url=url,
        modules={"models": ["app.database.models"]},
        generate_schemas=True,
        add_exception_handlers=True,
    )

app.include_router(healthcheck, tags=["healthcheck"])
app.include_router(tokens, tags=["tokens"])
