from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + "s"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    created = Column(DateTime, nullable=False, default=datetime.utcnow)
    modified = Column(DateTime, nullable=False, onupdate=datetime.utcnow)
