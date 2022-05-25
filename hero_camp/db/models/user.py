from passlib.context import CryptContext
from sqlalchemy import Column, String

from hero_camp.db.models import Base

pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)

    def verify_password(self, password: str) -> bool:
        return pwd_ctx.verify(password, self.password_hash)

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_ctx.hash(password)
