from alembic import context
from sqlalchemy import create_engine

from hero_camp.db.models import Base
from hero_camp.settings import SETTINGS

config = context.config
config.set_main_option("sqlalchemy.url", SETTINGS.db_url.replace("+asyncpg", ""))


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=Base.metadata)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    url = config.get_main_option("sqlalchemy.url")
    engine = create_engine(url)
    with engine.connect() as connection:
        context.configure(connection=connection, target_metadata=Base.metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
