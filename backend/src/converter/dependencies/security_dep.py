import httpx
from typing import Dict, Any

from fastapi import Depends


from converter.core.config import settings
from converter.dependencies.exceptions import InvalidTokenError
from converter.security.token_bearer import AccessTokenBearer

oauth2_scheme = AccessTokenBearer(scheme_name="access_token")


async def login_required(token: str = Depends(oauth2_scheme)) -> Dict[str, Any]:
    """
    The token here is access_token. Since in authserver only access_token is
    parsed we will send dummy refresh_token.
    """
    header = {"Content-Type": "application/json"}
    body = {
        "access_token": token,
        "refresh_token": "dummy-token",
        "token_type": "Bearer"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=settings.AUTHSERVER_TOKEN_VERIFICATION_URL,
                headers=header,
                json=body
            )

        response_json = response.json()

        return response_json
    except httpx.HTTPStatusError:
        raise InvalidTokenError