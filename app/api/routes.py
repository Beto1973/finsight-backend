# app/api/routes.py

from fastapi import APIRouter, HTTPException
from app.services.data_loader import load_financial_data
from app.services.ratios import calculate_ratios
from app.services.scoring.scoring_engine import analyze_company
from app.services.explanation import explain

router = APIRouter()


@router.get("/analyze/{ticker}")
def analyze_ticker(ticker: str):
    try:
        raw_data = load_financial_data(ticker.upper())
        metrics = calculate_ratios(raw_data)
        analysis = analyze_company(metrics)
        explanation = explain(
            analysis["total_score"],
            analysis["pillars"]
        )

        return {
            "ticker": ticker.upper(),
            **analysis,
            **explanation
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

