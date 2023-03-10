from tortoise import Tortoise

from app.settings.config import (
    USER_POSTGRES,
    PASSWORD_POSTGRES,
    HOST_POSTGRES,
    PORT_POSTGRES,
    DATABASE_POSTGRES
)


async def init_database_models():
    url = "asyncpg://{user}:{password}@{host}:{port}/{database}".format(
        user=USER_POSTGRES,
        password=PASSWORD_POSTGRES,
        host=HOST_POSTGRES,
        port=PORT_POSTGRES,
        database=DATABASE_POSTGRES
    )
    await Tortoise.init(db_url=url, modules={"models": ["app.database.models"]})
    await Tortoise.generate_schemas()
