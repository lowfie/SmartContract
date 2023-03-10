import uvicorn
from tortoise import run_async

from app.settings.config import UVICORN_RELOAD
from app.database.utils import init_database_models

if __name__ == "__main__":
    run_async(init_database_models())
    uvicorn.run(
        app="app.api.register_endpoints:app",
        host="0.0.0.0",
        port=8000,
        reload=UVICORN_RELOAD
    )
