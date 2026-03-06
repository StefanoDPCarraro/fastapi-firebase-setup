import sys
import traceback
from contextlib import asynccontextmanager

import firebase_admin
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from firebase_admin import credentials

from src.domains.parents.controller import router as parents_controller

from .config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Inicialização usando o objeto de settings tipado
    if not firebase_admin._apps:
        cred = credentials.Certificate(settings.firebase_credentials_path)
        firebase_admin.initialize_app(cred)
    yield


app = FastAPI(
    title="VanGo API",
    description="API para gestão de transporte escolar (VanGo)",
    version="0.1.0",
    lifespan=lifespan,
)


@app.exception_handler(Exception)
async def catch_all_handler(request: Request, exc: Exception) -> JSONResponse:
    traceback.print_exc(file=sys.stderr)

    return JSONResponse(
        status_code=500,
        content={
            "status": "error",
            "message": str(exc),
            "type": exc.__class__.__name__,
        },
    )


# Registro dos domínios (Routers)
app.include_router(parents_controller)


@app.get("/health", tags=["Infrastructure"])
def health_check() -> dict[str, str]:
    """Endpoint para o Healthcheck do Docker."""
    return {"status": "ok", "environment": "development"}


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Bem-vindo à VanGo API. Acesse /docs para a documentação."}
