def normalize_yahoo(raw: dict, ticker: str) -> dict:
    financials = raw.get("financialData", {})
    stats = raw.get("defaultKeyStatistics", {})
    summary = raw.get("summaryDetail", {})

    return {
        "ticker": ticker,
        "currency": summary.get("currency", "USD"),

        # Income Statement
        "revenue": financials.get("totalRevenue"),
        "net_income": financials.get("netIncomeToCommon"),
        "ebitda": financials.get("ebitda"),
        "eps": stats.get("trailingEps"),

        # Balance Sheet
        "total_assets": financials.get("totalAssets"),
        "total_liabilities": financials.get("totalDebt"),
        "equity": None,  # Yahoo no lo expone directo
        "current_assets": financials.get("currentAssets"),
        "current_liabilities": financials.get("currentLiabilities"),
        "debt": financials.get("totalDebt"),

        # Cash Flow
        "free_cash_flow": financials.get("freeCashflow"),

        # Market
        "price": summary.get("regularMarketPrice"),
        "market_cap": summary.get("marketCap"),
        "pe": summary.get("trailingPE"),
        "pb": stats.get("priceToBook"),
        "ev_ebitda": stats.get("enterpriseToEbitda"),

        # Risk
        "beta": stats.get("beta"),
        "volatility": None,

        # Growth
        "revenue_growth": financials.get("revenueGrowth"),
        "earnings_growth": financials.get("earningsGrowth")
    }
