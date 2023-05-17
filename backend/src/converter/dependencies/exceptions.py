from fastapi import HTTPException, status

from converter.core.config import settings

class InvalidTokenError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid tokens provided.")
    
class InvalidFileNameHeaderError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail="Required `Filename` header.")
    
class MaxUploadSizeExceedError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Max upload is {settings.FILE_MAX_SIZE} bytes.")

class FileUploadError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="There was an error uploading file.")
    
class FileNotPresentError(HTTPException):
    def __init__(self) -> None:
        return super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="File not found.")