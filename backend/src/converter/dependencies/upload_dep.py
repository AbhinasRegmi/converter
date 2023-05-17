import os
from uuid import uuid4
from typing import Dict

from fastapi import Request
from streaming_form_data import StreamingFormDataParser
from streaming_form_data.targets import FileTarget, ValueTarget

from converter.core.config import settings
from converter.dependencies.exceptions import FileUploadError
from converter.dependencies.exceptions import MaxUploadSizeExceedError
from converter.dependencies.exceptions import InvalidFileNameHeaderError
from converter.core.validators import MaxBodySizeValidator, MaxBodySizeException


class StreamingFileUpload:
    def __init__(self) -> None:
        self._validator = MaxBodySizeValidator(settings.FILE_REQUEST_BODY_MAX_SIZE)

    async def __call__(self, request: Request) -> Dict[str, str]:
        filename = request.headers.get('Filename')
        
        if not filename:
            raise InvalidFileNameHeaderError
        
        filename = str(uuid4())
        
        try:
            filepath = os.path.join(settings.FILE_UPLOAD_PATH, os.path.basename(filename))
            file_ = FileTarget(filepath, validator=self._validator)
            data = ValueTarget()
            parser = StreamingFormDataParser(headers=request.headers)
            parser.register('file', file_)
            parser.register('data', data)

            async for chunck in request.stream():
                parser.data_received(chunck)

            if not (file_name:=file_.multipart_filename):
                raise FileNotFoundError
            
            return {
                "filename": file_name,
                "uuid_file": filename
            }

        except MaxBodySizeException:
            raise MaxUploadSizeExceedError

        except:
            raise FileUploadError

async def sfileupload(request: Request) -> Dict[str, str]:
    dep = StreamingFileUpload()
    return await dep(request)