from portfolio.portfolio_engine import build_portfolio

mock_results = [
    {
        "ticker": "AAPL",
        "score": 0.82,
        "decision": "BUY",
        "pillars": {"risk": 0.30}
    },
    {
        "ticker": "MSFT",
        "score": 0.78,
        "decision": "BUY",
        "pillars": {"risk": 0.25}
    },
    {
        "ticker": "TSLA",
        "score": 0.60,
        "decision": "HOLD",
        "pillars": {"risk": 0.65}
    }
]

portfolio = build_portfolio(mock_results)

print(portfolio)
