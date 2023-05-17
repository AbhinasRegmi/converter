from starlette.requests import Request
from fastapi.security import HTTPBearer

from converter.security.exceptions import AuthorizationHeaderError


class AccessTokenBearer(HTTPBearer):
    async def __call__(self, request: Request) -> str:
        credentials = await super().__call__(request)

        if not credentials:
            raise AuthorizationHeaderError
        
        return credentials.credentials