from datetime import datetime, timedelta
from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from hero_camp.api.schemas import AccessToken, Claims
from hero_camp.settings import SETTINGS


class AuthScheme(HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials:
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(
                detail="Missing authorization header.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        scheme, _, credentials = auth_header.partition(" ")
        if scheme.lower() != "bearer":
            raise HTTPException(
                detail="Unsupported authorization scheme.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)


auth_scheme = AuthScheme(
    scheme_name="HTTPBearer", description="JWT authorization using the Bearer scheme."
)


def create_access_token(user_id: UUID) -> AccessToken:
    iat = datetime.utcnow()
    exp = iat + timedelta(minutes=SETTINGS.jwt_lifetime_in_minutes)
    claims = Claims(uid=user_id.hex, iat=iat, exp=exp)
    token = jwt.encode(claims.dict(), SETTINGS.jwt_secret_key, SETTINGS.jwt_algorithm)
    return AccessToken(token=token, token_type="Bearer", issued_at=iat, expired_in=exp)


def verify_access_token(
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
) -> Claims:
    try:
        claims: Claims = jwt.decode(
            token.credentials, SETTINGS.jwt_secret_key, SETTINGS.jwt_algorithm
        )
        return claims
    except jwt.DecodeError:
        raise HTTPException(
            detail="Invalid access token.", status_code=status.HTTP_401_UNAUTHORIZED
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            detail="Access token expired.", status_code=status.HTTP_401_UNAUTHORIZED
        )
