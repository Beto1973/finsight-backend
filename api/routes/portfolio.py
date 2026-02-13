from fastapi import APIRouter, Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
import logging

from portfolio.portfolio_engine import build_portfolio


router = APIRouter()

limiter = Limiter(key_func=get_remote_address)

logger = logging.getLogger("finsight.portfolio")


@router.post("/")
@limiter.limit("5/minute")
def create_portfolio(
    request: Request,
    tickers: list[str],
    capital: float
):
    try:
        if not tickers:
            raise HTTPException(status_code=400, detail="Lista de tickers vacía")

        if capital <= 0:
            raise HTTPException(status_code=400, detail="Capital debe ser mayor a cero")

        portfolio = build_portfolio(
            tickers=tickers,
            capital=capital
        )

        return portfolio

    except HTTPException:
        raise
    except Exception:
        logger.exception("Error en create_portfolio endpoint")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

