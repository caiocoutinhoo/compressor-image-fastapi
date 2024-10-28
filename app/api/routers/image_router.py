from fastapi import APIRouter, UploadFile, File
from typing import List
from fastapi.responses import StreamingResponse
from services.image_service import compress_images_service

router = APIRouter()

@router.post("/compress")
async def compress_images_endpoint(files: List[UploadFile] = File(...)):
    """
    Endpoint para receber imagens e retornar um arquivo ZIP com as imagens comprimidas.
    """
    zip_stream = await compress_images_service(files)
    return StreamingResponse(
        zip_stream,
        media_type="application/x-zip-compressed",
        headers={"Content-Disposition": "attachment; filename=compressed_images.zip"}
    )
