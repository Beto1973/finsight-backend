from intelligence.intelligence_engine import run_intelligence_layer

portfolio = {
    "allocations": [
        {"ticker": "AAPL", "weight": 0.40, "risk": 0.30},
        {"ticker": "MSFT", "weight": 0.35, "risk": 0.25}
    ],
    "portfolio_risk": 0.32
}

result = run_intelligence_layer(portfolio)

print(result)
