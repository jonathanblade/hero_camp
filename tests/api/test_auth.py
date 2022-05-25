import pytest
from fastapi import status


@pytest.mark.asyncio
async def test_auth(client):
    response = await client.post(
        "/api/auth/token", json={"username": "foo", "password": "foo"}
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    response = await client.post(
        "/api/auth/token", json={"username": "root", "password": "root"}
    )
    assert response.status_code == status.HTTP_201_CREATED
