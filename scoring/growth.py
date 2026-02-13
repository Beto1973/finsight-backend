from config.benchmarks import BENCHMARKS

def growth_score(data):
    score = 0
    b = BENCHMARKS["growth"]

    score += min(data["revenue_growth"] / b["revenue_growth"], 1) if data["revenue_growth"] else 0
    score += min(data["earnings_growth"] / b["earnings_growth"], 1) if data["earnings_growth"] else 0

    return round(score / 2 * 100, 2)

