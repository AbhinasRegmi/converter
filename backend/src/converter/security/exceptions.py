from fastapi import HTTPException, status


class AuthorizationHeaderError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization Header Absent")
    

class BearerTypeTokenRequiredError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Authorization type should be bearer")