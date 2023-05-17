from fastapi import HTTPException, status


class FileNameNotFoundError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="FileName required in Header."
        )