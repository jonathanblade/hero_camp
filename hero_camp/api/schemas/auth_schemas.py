from datetime import datetime

from pydantic import BaseModel, Field


class Claims(BaseModel):
    uid: str = Field(description="User ID.")
    iat: datetime = Field(description="Access token issuing time (UTC).")
    exp: datetime = Field(description="Access token expiring time (UTC).")


class Credentials(BaseModel):
    username: str = Field(description="Username.", example="root")
    password: str = Field(description="Password.", example="root")


class AccessToken(BaseModel):
    token: str = Field(
        description="Access token.",
        example="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0MSIsInNjb3BlcyI6WyJhbGwiXSwiZXhwIjoxNjIzMjU1NTY3fQ.MJJe4b9UmpB7fiRasuv5dMESKyc6LJ-IQtt5X7nJ4bY",
    )
    token_type: str = Field(description="Access token type.", default="Bearer")
    issued_at: datetime = Field(
        description="Access token issuing time (UTC).",
        example="2022-05-26T08:42:49.190774",
    )
    expired_in: datetime = Field(
        description="Access token expiring time (UTC).",
        example="2022-05-26T09:42:49.190774",
    )
