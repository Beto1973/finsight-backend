from fastapi import FastAPI
from app.api.analyze import router as analyze_router

app = FastAPI(
    title="FinSight API",
    description="Plataforma de Análisis Financiero Inteligente",
    version="0.1.0"
)

app.include_router(analyze_router)


# python -m uvicorn api.main:app --reload
# http://127.0.0.1:8000/docs
# http://127.0.0.1:8000/openapi.json
