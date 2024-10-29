from fastapi import FastAPI
from app.api.routers.image_router import router as image_router
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="API de Compressão de Imagens")
app.mount("/img", StaticFiles(directory="img"), name="img")

app.include_router(image_router, prefix="/images", tags=["Images"])

@app.get("/")
async def read_index():
    return FileResponse("index.html")  # Serve o arquivo index.html

