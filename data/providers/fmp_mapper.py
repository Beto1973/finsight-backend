def map_fmp(raw: dict) -> dict:
    return {
        "currency": raw.get("currency"),
        "revenue": raw.get("revenue"),
        "net_income": raw.get("netIncome"),
        "operating_income": raw.get("operatingIncome"),
        "total_assets": raw.get("totalAssets"),
        "total_liabilities": raw.get("totalLiabilities"),
        "equity": raw.get("totalStockholdersEquity"),
        "debt": raw.get("totalDebt"),
        "cash": raw.get("cashAndCashEquivalents"),
        "current_assets": raw.get("totalCurrentAssets"),
        "current_liabilities": raw.get("totalCurrentLiabilities"),
        "operating_cash_flow": raw.get("operatingCashFlow"),
        "free_cash_flow": raw.get("freeCashFlow"),
        "market_cap": raw.get("marketCap"),
        "price": raw.get("price"),
        "shares_outstanding": raw.get("sharesOutstanding"),
        "pe": raw.get("pe"),
        "pb": raw.get("pb"),
        "ev_ebitda": raw.get("enterpriseValueOverEBITDA"),
        "revenue_growth": raw.get("revenueGrowth"),
        "earnings_growth": raw.get("earningsGrowth"),
        "fcf_growth": raw.get("freeCashFlowGrowth"),
        "beta": raw.get("beta"),
        "volatility": raw.get("volatility"),
        "max_drawdown": raw.get("maxDrawdown"),
    }


def normalize_fmp(raw: dict, ticker: str) -> dict:
    return map_fmp(raw)
