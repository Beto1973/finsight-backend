from data.normalized_data import normalize_financials


def test_normalization_schema():
    raw = {
        "revenue": 100,
        "net_income": 20,
        "free_cash_flow": 15,
        "market_cap": 1000,
        "price": 150,
        "beta": 1.1
    }

    n = normalize_financials(raw, "mock", "AAPL")

    assert n["ticker"] == "AAPL"
    assert "revenue" in n
    assert n["data_quality_score"] > 0
