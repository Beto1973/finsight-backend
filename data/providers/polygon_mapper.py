def map_polygon(raw: dict) -> dict:
    """
    Normaliza payload de Polygon.io al esquema financiero canónico.
    Polygon NO es tan fundamental-heavy como FMP / Alpha,
    se mapea lo disponible sin inventar datos.
    """

    financials = raw.get("financials", {})
    company = raw.get("company", {})
    metrics = raw.get("metrics", {})

    return {
        "company": {
            "name": company.get("name"),
            "sector": company.get("sector"),
            "industry": company.get("industry"),
            "country": company.get("locale"),
            "currency": company.get("currency_name"),
        },
        "valuation": {
            "market_cap": _to_float(metrics.get("market_cap")),
            "pe_ratio": _to_float(metrics.get("pe_ratio")),
            "price_to_book": _to_float(metrics.get("price_to_book")),
        },
        "profitability": {
            "revenue": _to_float(financials.get("revenue")),
            "net_income": _to_float(financials.get("net_income")),
            "roe": _to_float(metrics.get("roe")),
            "roa": _to_float(metrics.get("roa")),
        },
        "financial_health": {
            "total_assets": _to_float(financials.get("assets")),
            "total_liabilities": _to_float(financials.get("liabilities")),
            "total_equity": _to_float(financials.get("equity")),
            "debt_to_equity": _to_float(metrics.get("debt_to_equity")),
        },
        "cash_flow": {
            "operating_cash_flow": _to_float(financials.get("operating_cash_flow")),
            "free_cash_flow": _to_float(financials.get("free_cash_flow")),
        }
    }


def _to_float(value):
    try:
        return float(value)
    except Exception:
        return None


def normalize_polygon(raw: dict, ticker: str) -> dict:
    return map_polygon(raw)
