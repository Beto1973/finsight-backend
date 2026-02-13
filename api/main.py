from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from api.routes.analyze import router as analyze_router
from api.routes.portfolio import router as portfolio_router
from api.routes.intelligence import router as intelligence_router

from api.security import verify_platform_key
from config.settings import settings

from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

import logging


# -------------------------------------------------------------------
# LOGGING PROFESIONAL
# -------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

logger = logging.getLogger("finsight")


# -------------------------------------------------------------------
# VALIDACIONES CRÍTICAS DE ENTORNO
# -------------------------------------------------------------------

if settings.ENV == "production":
    if not settings.PLATFORM_API_KEY:
        raise RuntimeError("PLATFORM_API_KEY requerida en producción")

    if not settings.ALLOWED_ORIGINS:
        raise RuntimeError("ALLOWED_ORIGINS debe estar configurado en producción")


# -------------------------------------------------------------------
# RATE LIMITER GLOBAL
# -------------------------------------------------------------------

limiter = Limiter(key_func=get_remote_address)


# -------------------------------------------------------------------
# INICIALIZACIÓN FASTAPI
# -------------------------------------------------------------------

app = FastAPI(
    title="FinSight – Investment with Intelligence",
    description="Plataforma de Análisis y Asignación de Capital",
    version="1.0.0",
    docs_url=None if settings.ENV == "production" else "/docs",
    redoc_url=None if settings.ENV == "production" else "/redoc",
    openapi_url=None if settings.ENV == "production" else "/openapi.json",
    dependencies=[Depends(verify_platform_key)] if settings.ENV == "production" else []
)

@app.get("/")
def root():
    return {"service": "FinSight API", "status": "online"}


# -------------------------------------------------------------------
# CORS PROFESIONAL POR ENTORNO
# -------------------------------------------------------------------

if settings.ENV == "production":
    allowed_origins = [
        origin.strip()
        for origin in settings.ALLOWED_ORIGINS.split(",")
        if origin.strip()
    ]
else:
    allowed_origins = [
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


# -------------------------------------------------------------------
# RATE LIMITING MIDDLEWARE
# -------------------------------------------------------------------

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request, exc):
    return JSONResponse(
        status_code=429,
        content={"detail": "Rate limit exceeded"}
    )


# -------------------------------------------------------------------
# ROUTERS (SIN MODIFICAR LÓGICA)
# -------------------------------------------------------------------

app.include_router(analyze_router, prefix="/analyze", tags=["Analysis"])
app.include_router(portfolio_router, prefix="/portfolio", tags=["Portfolio"])
app.include_router(intelligence_router, prefix="/intelligence", tags=["Intelligence"])

