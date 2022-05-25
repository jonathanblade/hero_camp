from typing import Type, TypedDict

from pydantic import BaseModel

from hero_camp.api.schemas import HTTPError


class ResponseType(TypedDict):
    description: str
    model: Type[BaseModel]


def post_request_responses(model: Type[BaseModel]) -> dict[int, ResponseType]:
    return {
        201: {"description": "Created", "model": model},
        400: {"description": "Bad request", "model": HTTPError},
        401: {"description": "Unauthorized", "model": HTTPError},
        500: {"description": "Internal server error", "model": HTTPError},
    }
