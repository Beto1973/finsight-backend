# finsight/portfolio/risk_control.py

def portfolio_risk(allocations: list[dict]) -> float:
    """
    Riesgo agregado ponderado
    """
    if not allocations:
        return 0

    return round(
        sum(a["risk"] * a["weight"] for a in allocations),
        4
    )
