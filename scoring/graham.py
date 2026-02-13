# finsight/scoring/graham.py

def graham_score(data: dict) -> float:
    """
    Modelo Benjamin Graham:
    Margen de seguridad
    """

    rules = 0

    pe = data.get("pe")
    pb = data.get("pb")
    debt = data.get("debt_to_equity")
    current = data.get("current_ratio")
    eps_growth = data.get("eps_cagr")

    if pe and pe <= 15:
        rules += 1

    if pb and pb <= 1.5:
        rules += 1

    if debt is not None and debt < 1:
        rules += 1

    if current and current >= 2:
        rules += 1

    if eps_growth and eps_growth > 0:
        rules += 1

    return round((rules / 5) * 100, 2)
