import uvicorn

from app.settings.config import UVICORN_RELOAD, UVICORN_HOST

if __name__ == "__main__":
    uvicorn.run(
        app="app.api.register_endpoints:app",
        host=UVICORN_HOST,
        port=8000,
        reload=UVICORN_RELOAD
    )
