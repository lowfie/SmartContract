import uvicorn
from tortoise import run_async

from app.settings.config import UVICORN_RELOAD, UVICORN_HOST
from app.database.utils import init_database_models

if __name__ == "__main__":
    run_async(init_database_models())
    uvicorn.run(
        app="app.api.register_endpoints:app",
        host=UVICORN_HOST,
        port=8000,
        reload=UVICORN_RELOAD
    )
