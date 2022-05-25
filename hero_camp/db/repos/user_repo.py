from sqlalchemy.ext.asyncio import AsyncSession

from hero_camp.db.models import User
from hero_camp.db.repos import CRUDRepo


class UserRepo(CRUDRepo):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(User, session)
