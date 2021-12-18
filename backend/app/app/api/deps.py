import logging
from typing import Generator

from fastapi import Depends
from keycloak import KeycloakOpenID

from sqlalchemy.orm import Session

from app import crud, models
from app.core.config import settings
from app.db.session import SessionLocal

from fastapi.security import OAuth2AuthorizationCodeBearer
from fastapi import Security, HTTPException, status
from pydantic import Json

logger = logging.getLogger(__name__)


# This is just for fastapi docs
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.AUTH_SERVER_URL}/auth/realms/{settings.AUTH_REALM}/protocol/openid-connect/auth",
    tokenUrl=f"{settings.AUTH_SERVER_URL}/auth/realms/{settings.AUTH_REALM}/protocol/openid-connect/token",
)

# Auth checks, not sure that all that methods are truly async
keycloak_openid = KeycloakOpenID(
    server_url=settings.INTERNAL_AUTH_SERVER_URL,
    client_id=settings.AUTH_CLIENT_ID,
    realm_name=settings.AUTH_REALM,
    verify=True,
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_idp_public_key():
    return (
        "-----BEGIN PUBLIC KEY-----\n"
        f"{keycloak_openid.public_key()}"
        "\n-----END PUBLIC KEY-----"
    )


async def get_current_user(
        db: Session = Depends(get_db),
        token: str = Security(oauth2_scheme)) -> Json:
    try:
        token_data = keycloak_openid.decode_token(
            token,
            key=await get_idp_public_key(),
            options={"verify_signature": True, "verify_aud": False, "exp": True},
        )
    except Exception as e:
        logger.error(str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = crud.user.get_by_email(db, email=token_data["preferred_username"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def get_current_active_user(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_active(current_user):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def get_current_active_superuser(
    current_user: models.User = Depends(get_current_user),
) -> models.User:
    if not crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
