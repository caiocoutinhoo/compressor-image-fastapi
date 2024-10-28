from fastapi import FastAPI
from app.api.routers.image_router import router as image_router

app = FastAPI(title="API de Compressão de Imagens")

app.include_router(image_router, prefix="/images", tags=["Images"])
