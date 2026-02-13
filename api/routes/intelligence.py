from fastapi import APIRouter, Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
import logging

from intelligence.intelligence_engine import run_intelligence_layer


router = APIRouter()

limiter = Limiter(key_func=get_remote_address)

logger = logging.getLogger("finsight.intelligence")


@router.post("/")
@limiter.limit("5/minute")
def intelligence_layer(
    request: Request,
    portfolio: dict
):
    try:
        if not portfolio:
            raise HTTPException(status_code=400, detail="Portfolio vacío")

        result = run_intelligence_layer(portfolio)

        return result

    except HTTPException:
        raise
    except Exception:
        logger.exception("Error en intelligence_layer endpoint")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
