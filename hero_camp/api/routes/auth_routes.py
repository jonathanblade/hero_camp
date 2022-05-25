from fastapi import APIRouter, Depends, HTTPException, status

from hero_camp.api.deps import get_user_repo
from hero_camp.api.responses import post_request_responses
from hero_camp.api.schemas import AccessToken, Credentials
from hero_camp.api.security import create_access_token
from hero_camp.db.repos import UserRepo

router = APIRouter()


@router.post(
    "/token",
    status_code=201,
    name="Create new access token.",
    responses=post_request_responses(AccessToken),
)
async def token(
    credentials: Credentials, user_repo: UserRepo = Depends(get_user_repo)
) -> AccessToken:
    user = await user_repo.get_by_field("username", credentials.username)
    if not user:
        raise HTTPException(
            detail="Invalid credentials.", status_code=status.HTTP_401_UNAUTHORIZED
        )
    if not user.verify_password(credentials.password):
        raise HTTPException(
            detail="Invalid credentials.", status_code=status.HTTP_401_UNAUTHORIZED
        )
    return create_access_token(user.id)
