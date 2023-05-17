from uuid import uuid4

from fastapi import Request

class FileService:
    @classmethod
    async def upload_file(cls, filename: str, request: Request) -> None:
        """
        Upload file upto max-size 3Gb. Saves the file to
        system memory at root of the server.
        """
        unique_filename: str = filename + str(uuid4())
        
        