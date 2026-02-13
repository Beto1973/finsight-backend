# finsight/scoring/lynch.py

def lynch_score(data: dict) -> float:
    """
    Modelo Peter Lynch:
    Crecimiento razonable (GARP)
    """

    pe = data.get("pe")
    eps_growth = data.get("eps_cagr")
    revenue_growth = data.get("revenue_cagr")
    debt = data.get("debt_to_equity")

    score = 0

    if pe and eps_growth and eps_growth > 0:
        peg = pe / (eps_growth * 100)
        score += max(1 - abs(peg - 1), 0) * 40

    if eps_growth:
        score += min(eps_growth / 0.15, 1) * 30

    if revenue_growth:
        score += min(revenue_growth / 0.10, 1) * 20

    if debt is not None:
        score += max(1 - debt, 0) * 10

    return round(min(score, 100), 2)
