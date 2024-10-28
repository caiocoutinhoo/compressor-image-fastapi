from typing import List
from fastapi import UploadFile
from app.utils.image_compression import compress_images_to_zip

async def compress_images_service(files: List[UploadFile]):
    """
    Serviço que orquestra a compressão das imagens.
    """
    return await compress_images_to_zip(files)
