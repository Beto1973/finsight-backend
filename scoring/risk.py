# scoring/risk.py

def risk_score(data: dict) -> float:
    """
    Score de riesgo (0–100).
    Bajo riesgo = score alto.
    """

    beta = data.get("beta", 1.0)
    volatility = data.get("volatility", 0.3)

    beta_norm = min(max((beta - 0.5) / 1.5, 0), 1)
    vol_norm = min(max((volatility - 0.1) / 0.5, 0), 1)

    risk_level = (0.6 * beta_norm) + (0.4 * vol_norm)

    score = 100 * (1 - risk_level)

    # Boost conservador
    if beta < 1 and volatility < 0.2:
        score += 10

    return round(min(max(score, 0), 100), 2)


