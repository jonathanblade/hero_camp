"""Initial revision

Revision ID: 03842e36cc31
Revises:
Create Date: 2022-05-25 10:30:11.611313

"""
from datetime import datetime
from uuid import uuid4

from alembic import op
from sqlalchemy import Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID

from hero_camp.db.models import User
from hero_camp.settings import SETTINGS

revision = "03842e36cc31"
down_revision = None
branch_labels = None
depends_on = None


def create_superuser():
    username = SETTINGS.superuser_username
    password_hash = User.hash_password(SETTINGS.superuser_password)
    created = datetime.utcnow()
    op.execute(
        f"INSERT INTO users VALUES ('{uuid4()}', '{created}', '{created}', '{username}', '{password_hash}')"
    )


def upgrade():
    op.create_table(
        "users",
        Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        Column("created", DateTime, nullable=False, default=datetime.utcnow),
        Column("modified", DateTime, nullable=False, onupdate=datetime.utcnow),
        Column("username", String, nullable=False, unique=True),
        Column("password_hash", String, nullable=False),
    )
    create_superuser()


def downgrade():
    op.drop_table("users")
