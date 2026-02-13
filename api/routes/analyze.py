from fastapi import APIRouter, Query
from data.data_loader import load_company_data
from data.normalize import normalize_financials
from data.ratios import calculate_ratios
from core.scoring_engine import analyze_company
from core.explanation_engine import generate_explanation
from decision.alerts import generate_alerts

from fastapi import HTTPException
from core.exceptions import InvalidTickerError


router = APIRouter()

@router.get("/")
def analyze_company_endpoint(
    ticker: str = Query(...),
    use_mock: bool = Query(False)
):
    try:
        raw = load_company_data(ticker)
    except InvalidTickerError as e:
        raise HTTPException(
            status_code=400,
            detail={
                "error": "INVALID_TICKER",
                "ticker": e.ticker,
                "message": f"No se pudo obtener información para el ticker '{e.ticker}'.",
                "hint": "Verifique si el símbolo es correcto (ej: Bank of America = BAC)."
            }
        )

    payload = raw["data"] if isinstance(raw, dict) and "data" in raw else raw
    provider = raw["provider"] if isinstance(raw, dict) and "provider" in raw else "mock"

    normalized = normalize_financials(
        raw=payload,
        provider=provider,
        ticker=ticker
    )

    ratios = calculate_ratios(normalized)
    scoring = analyze_company(ratios)
    alerts = generate_alerts(ratios, scoring["pillars"])
    explanation = generate_explanation(scoring)

    return {
        "ticker": ticker,
        "provider": provider,
        "ratios": ratios,
        "scoring": scoring,
        "alerts": alerts,
        "explanation": explanation
    }


