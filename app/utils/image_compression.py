from typing import List
from fastapi import UploadFile
import io
import zipfile
from PIL import Image

async def compress_images_to_zip(files: List[UploadFile]) -> io.BytesIO:
    """
    Função utilitária que comprime imagens e as adiciona a um arquivo ZIP em memória.
    """
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            contents = await file.read()
            image = Image.open(io.BytesIO(contents))

            # Comprimir a imagem ajustando a qualidade
            output_io = io.BytesIO()
            image.save(output_io, format='JPEG', quality=70)
            output_io.seek(0)

            # Adicionar a imagem comprimida ao ZIP
            zip_file.writestr(file.filename, output_io.read())

    zip_buffer.seek(0)
    return zip_buffer
