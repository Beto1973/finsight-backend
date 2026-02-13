# finsight/data/normalized_data.py

from typing import Dict
from data.schema import NormalizedFinancials


def normalize_financials(
    raw: Dict,
    provider: str,
    ticker: str
) -> NormalizedFinancials:
    """
    Convierte data cruda de cualquier provider
    al modelo financiero canónico.
    """

    n = NormalizedFinancials()

    n["ticker"] = ticker
    n["provider"] = provider
    n["currency"] = raw.get("currency")

    # ---------- INCOME ----------
    n["revenue"] = raw.get("revenue")
    n["net_income"] = raw.get("net_income")
    n["operating_income"] = raw.get("operating_income")

    # ---------- BALANCE ----------
    n["total_assets"] = raw.get("total_assets")
    n["total_liabilities"] = raw.get("total_liabilities")
    n["equity"] = raw.get("equity")
    n["debt"] = raw.get("debt")
    n["cash"] = raw.get("cash")
    n["current_assets"] = raw.get("current_assets")
    n["current_liabilities"] = raw.get("current_liabilities")

    # ---------- CASH FLOW ----------
    n["operating_cash_flow"] = raw.get("operating_cash_flow")
    n["free_cash_flow"] = raw.get("free_cash_flow")

    # ---------- MARKET ----------
    n["market_cap"] = raw.get("market_cap")
    n["price"] = raw.get("price")
    n["shares_outstanding"] = raw.get("shares_outstanding")

    # ---------- VALUATION ----------
    n["pe"] = raw.get("pe")
    n["pb"] = raw.get("pb")
    n["ev_ebitda"] = raw.get("ev_ebitda")

    # ---------- GROWTH ----------
    n["revenue_growth"] = raw.get("revenue_growth")
    n["earnings_growth"] = raw.get("earnings_growth")
    n["fcf_growth"] = raw.get("fcf_growth")

    # ---------- RISK ----------
    n["beta"] = raw.get("beta")
    n["volatility"] = raw.get("volatility")
    n["max_drawdown"] = raw.get("max_drawdown")

    # ---------- DATA QUALITY ----------
    n["data_quality_score"] = calculate_data_quality(n)

    return n


def calculate_data_quality(n: Dict) -> float:
    """
    Score simple de calidad de data (0–1).
    Penaliza campos críticos faltantes.
    """

    critical_fields = [
        "revenue",
        "net_income",
        "free_cash_flow",
        "market_cap",
        "price",
        "beta"
    ]

    available = sum(1 for f in critical_fields if n.get(f) is not None)
    return round(available / len(critical_fields), 2)
