from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.services.api.routes import status


def create_app() -> FastAPI:
    app = FastAPI(title="Main API")

    app.include_router(status.router)

    @app.get("/", include_in_schema=False)
    async def root():
        return RedirectResponse(url="/docs", status_code=302)

    return app
