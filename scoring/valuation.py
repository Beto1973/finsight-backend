from config.benchmarks import BENCHMARKS

def valuation_score(data):
    score = 0
    b = BENCHMARKS["valuation"]

    if data["pe"]:
        score += 1 if data["pe"] <= b["pe"] else b["pe"] / data["pe"]

    if data["pb"]:
        score += 1 if data["pb"] <= b["pb"] else b["pb"] / data["pb"]

    return round(score / 2 * 100, 2)
