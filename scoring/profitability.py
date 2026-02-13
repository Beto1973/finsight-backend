from config.benchmarks import BENCHMARKS

def profitability_score(data):
    score = 0
    b = BENCHMARKS["profitability"]

    score += min(data["roe"] / b["roe"], 1) if data["roe"] else 0
    score += min(data["net_margin"] / b["net_margin"], 1) if data["net_margin"] else 0
    score += min(data["roa"] / b["roa"], 1) if data["roa"] else 0

    return round(score / 3 * 100, 2)
