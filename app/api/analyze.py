from fastapi import APIRouter, Query, Request, HTTPException
from slowapi import Limiter
from slowapi.util import get_remote_address
import logging

from data.data_loader import load_company_data
from data.mock_data import load_mock_company_data
from data.ratios import calculate_ratios

from core.scoring_engine import analyze_company
from core.explanation_engine import generate_explanation

from decision.decision_engine import investment_decision
from decision.alerts import generate_alerts
from decision.rating import assign_rating


router = APIRouter()

limiter = Limiter(key_func=get_remote_address)

logger = logging.getLogger("finsight.analyze")


@router.get("/analyze")
@limiter.limit("10/minute")
def analyze(
    request: Request,
    ticker: str = Query(..., description="Ticker bursátil"),
    use_mock: bool = Query(False, description="Usar datos mock")
):
    try:
        # 1️⃣ Carga de datos
        if use_mock:
            raw_data = load_mock_company_data(ticker)
            provider = "mock"
            data = raw_data
        else:
            raw = load_company_data(ticker)
            provider = raw.get("provider")
            data = raw.get("data")
            raw_data = raw  # consistencia estructural

        if not data:
            raise HTTPException(status_code=404, detail="Datos no encontrados")

        # 2️⃣ Cálculo de ratios
        ratios = calculate_ratios(data)

        # 3️⃣ Scoring
        result = analyze_company(ratios)
        rating = assign_rating(result["score"])

        decision = investment_decision(
            score=result["score"],
            risk_score=result["pillars"]["risk"]
        )

        alerts = generate_alerts(
            ratios=ratios,
            model_scores=result["models"]
        )

        # 4️⃣ Explicación
        explanation = generate_explanation(result)

        # 5️⃣ Respuesta API
        return {
            "ticker": ticker,
            "source": raw_data.get("source") if isinstance(raw_data, dict) else provider,
            "score": result["score"],
            "rating": rating,
            "decision": decision,
            "pillars": result["pillars"],
            "models": result["models"],
            "alerts": alerts,
            "explanation": explanation
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Error en analyze endpoint")
        raise HTTPException(status_code=500, detail="Error interno del servidor")


