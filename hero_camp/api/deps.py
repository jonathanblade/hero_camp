from functools import lru_cache

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from hero_camp.api.schemas import Claims
from hero_camp.api.security import auth_scheme
from hero_camp.db import Session
from hero_camp.db.repos import UserRepo
from hero_camp.settings import SETTINGS


async def get_session() -> AsyncSession:
    async with Session() as session:
        yield session


@lru_cache()
def get_user_repo(session: UserRepo = Depends(get_session)) -> UserRepo:
    return UserRepo(session)
