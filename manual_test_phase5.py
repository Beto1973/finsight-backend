from core.explanation_engine import generate_explanation

mock_result = {
    "score": 0.78,
    "rating": "BUY",
    "decision": "Invertir",
    "pillars": {
        "profitability": 0.82,
        "growth": 0.75,
        "solvency": 0.90,
        "valuation": 0.65,
        "risk": 0.30
    },
    "models": {
        "buffett": 0.80,
        "graham": 0.72,
        "lynch": 0.76
    },
    "alerts": ["Valuación exigente"]
}

print(generate_explanation(mock_result))
