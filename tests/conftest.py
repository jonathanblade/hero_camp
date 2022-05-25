import pytest_asyncio
from async_asgi_testclient import TestClient

from hero_camp.asgi import app
from hero_camp.db import downgrade_db


@pytest_asyncio.fixture
async def client():
    async with TestClient(app) as client:
        yield client
    downgrade_db()
