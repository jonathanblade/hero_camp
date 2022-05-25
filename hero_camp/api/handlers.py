from fastapi import Request, Response, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException


async def http_404_handler(request: Request, _exc: HTTPException) -> Response:
    return JSONResponse(
        content={"detail": f"Resource at '{request.url}' not found."},
        status_code=status.HTTP_404_NOT_FOUND,
    )


async def http_405_handler(_request: Request, _exc: HTTPException) -> Response:
    return JSONResponse(
        content={"detail": "Method not allowed."},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


async def http_422_handler(_request: Request, _exc: RequestValidationError) -> Response:
    return JSONResponse(
        content={"detail": "Malformed request payload."},
        status_code=status.HTTP_400_BAD_REQUEST,
    )


exception_handlers = {
    status.HTTP_404_NOT_FOUND: http_404_handler,
    status.HTTP_405_METHOD_NOT_ALLOWED: http_405_handler,
    RequestValidationError: http_422_handler,
}
