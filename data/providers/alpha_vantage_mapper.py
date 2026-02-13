def map_alpha_vantage(raw: dict) -> dict:
    """
    Normaliza payload de Alpha Vantage al esquema financiero canónico.
    NO calcula ratios
    NO hace scoring
    NO valida negocio
    """

    overview = raw.get("overview", {})
    income = raw.get("income_statement", {})
    balance = raw.get("balance_sheet", {})
    cashflow = raw.get("cash_flow", {})

    return {
        "company": {
            "name": overview.get("Name"),
            "sector": overview.get("Sector"),
            "industry": overview.get("Industry"),
            "country": overview.get("Country"),
            "currency": overview.get("Currency"),
        },
        "valuation": {
            "market_cap": _to_float(overview.get("MarketCapitalization")),
            "pe_ratio": _to_float(overview.get("PERatio")),
            "peg_ratio": _to_float(overview.get("PEGRatio")),
            "price_to_book": _to_float(overview.get("PriceToBookRatio")),
        },
        "profitability": {
            "revenue": _latest(income, "totalRevenue"),
            "gross_profit": _latest(income, "grossProfit"),
            "net_income": _latest(income, "netIncome"),
            "operating_margin": _to_float(overview.get("OperatingMarginTTM")),
            "profit_margin": _to_float(overview.get("ProfitMargin")),
            "roe": _to_float(overview.get("ReturnOnEquityTTM")),
            "roa": _to_float(overview.get("ReturnOnAssetsTTM")),
        },
        "financial_health": {
            "total_assets": _latest(balance, "totalAssets"),
            "total_liabilities": _latest(balance, "totalLiabilities"),
            "total_equity": _latest(balance, "totalShareholderEquity"),
            "current_ratio": _to_float(overview.get("CurrentRatio")),
            "debt_to_equity": _to_float(overview.get("DebtToEquity")),
        },
        "cash_flow": {
            "operating_cash_flow": _latest(cashflow, "operatingCashflow"),
            "free_cash_flow": _latest(cashflow, "freeCashflow"),
        }
    }


def _latest(section: dict, field: str):
    try:
        return float(section["annualReports"][0].get(field))
    except Exception:
        return None


def _to_float(value):
    try:
        return float(value)
    except Exception:
        return None


def normalize_alpha_vantage(raw: dict, ticker: str) -> dict:
    return map_alpha_vantage(raw)
