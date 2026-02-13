# finsight/scoring/buffett.py

def buffett_score(data: dict) -> float:
    """
    Modelo Warren Buffett:
    Calidad del negocio y retorno sostenible
    """

    roe = data.get("roe")
    roic = data.get("roic")
    margin = data.get("net_margin")
    debt = data.get("debt_to_equity")
    fcf = data.get("fcf_cagr")
    volatility = data.get("volatility")

    score = 0

    if roe:
        score += min(roe / 0.20, 1) * 25

    if roic:
        score += min(roic / 0.15, 1) * 20

    if margin:
        score += min(margin / 0.15, 1) * 15

    if fcf:
        score += min(fcf / 0.10, 1) * 15

    if debt is not None:
        score += max(1 - debt, 0) * 15

    if volatility:
        score += max(1 - volatility, 0) * 10

    return round(min(score, 100), 2)
