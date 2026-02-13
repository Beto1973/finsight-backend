# finsight/intelligence/stress_test.py

def stress_test_portfolio(portfolio: dict) -> dict:
    risk = portfolio["portfolio_risk"]

    if risk < 0.25:
        status = "ROBUST"
    elif risk < 0.45:
        status = "MODERATE"
    else:
        status = "FRAGILE"

    return {
        "portfolio_risk": risk,
        "stress_status": status
    }
