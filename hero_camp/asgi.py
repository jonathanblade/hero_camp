from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from hero_camp.api.handlers import exception_handlers
from hero_camp.api.middlewares import BadRequestMiddleware, ExceptionMiddleware
from hero_camp.api.routes import router
from hero_camp.db import upgrade_db
from hero_camp.settings import SETTINGS, Settings


def custom_openapi_schema(app: FastAPI) -> dict[str, Any]:
    """
    Кастомная OpenAPI схема, в которой вырезаны дефолтные 422 ошибки от FastAPI.
    Подробнее: https://github.com/tiangolo/fastapi/issues/1376
    """
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )

    del openapi_schema["components"]["schemas"]["ValidationError"]
    del openapi_schema["components"]["schemas"]["HTTPValidationError"]

    for method in openapi_schema["paths"]:
        try:
            del openapi_schema["paths"][method]["post"]["responses"]["422"]
        except KeyError:
            pass

    return openapi_schema


def on_startup() -> None:
    upgrade_db()


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        debug=settings.debug_mode,
        docs_url=settings.docs_url,
        redoc_url=None,
        exception_handlers=exception_handlers,
    )
    app.include_router(router, prefix=settings.api_prefix)
    app.add_middleware(ExceptionMiddleware)
    app.add_middleware(BadRequestMiddleware)
    app.add_event_handler("startup", on_startup)
    app.openapi_schema = custom_openapi_schema(app)
    return app


app = create_app(SETTINGS)


def start() -> None:
    uvicorn.run(
        "hero_camp.asgi:app",
        host=SETTINGS.app_host,
        port=SETTINGS.app_post,
        reload=True,
    )
