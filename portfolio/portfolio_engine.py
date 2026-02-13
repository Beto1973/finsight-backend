# finsight/portfolio/portfolio_engine.py

from portfolio.allocator import allocate_weights
from portfolio.risk_control import portfolio_risk


def build_portfolio(analysis_results: list[dict]) -> dict:
    """
    analysis_results: salida del analyze_company para múltiples tickers
    """

    assets = []

    for r in analysis_results:
        assets.append({
            "ticker": r["ticker"],
            "score": r["score"],
            "risk": r["pillars"].get("risk", 0),
            "decision": r["decision"]
        })

    allocations = allocate_weights(assets)
    risk = portfolio_risk(allocations)

    return {
        "allocations": allocations,
        "portfolio_risk": risk
    }
