from typing import Any, Optional, Type, TypeVar

from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from hero_camp.db.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDRepo:
    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get_by_field(self, field: str, value: Any) -> Optional[ModelType]:
        field = getattr(self.model, field)
        if field is None:
            raise AttributeError
        return await self.session.scalar(select(self.model).where(field == value))
