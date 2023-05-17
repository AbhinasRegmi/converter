import os
from typing import Dict, Any


from fastapi import Depends
from fastapi import APIRouter
from streaming_form_data import StreamingFormDataParser
from fastapi import Request, UploadFile, HTTPException, status
from streaming_form_data.targets import FileTarget, ValueTarget

from converter.dependencies.security_dep import login_required
from converter.dependencies.upload_dep import sfileupload
from converter.api.handlers.exceptions import FileNameNotFoundError

router = APIRouter()


@router.get("/upload")
async def upload(request: Request, user_data: Dict[str, Any] = Depends(login_required)):
    filename = request.headers.get("Filename")

    if not filename:
        raise FileNameNotFoundError
    

@router.post("/upload-using-fileupload")
def upload_using_fileupload(file: UploadFile):
    print(file.filename)
    return {"filename": file.filename}

@router.post("/upload-using-stream")
async def upload_using_stream(data =  Depends(sfileupload)):
    return data
    