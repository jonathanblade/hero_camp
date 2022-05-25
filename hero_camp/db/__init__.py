from alembic.command import downgrade, upgrade
from alembic.config import Config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from hero_camp.settings import SETTINGS

engine = create_async_engine(SETTINGS.db_url)
Session = sessionmaker(engine, class_=AsyncSession)
alembic_config = Config("alembic.ini")


def downgrade_db() -> None:
    downgrade(alembic_config, "base")


def upgrade_db() -> None:
    upgrade(alembic_config, "head")
