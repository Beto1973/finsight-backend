from config.benchmarks import BENCHMARKS

def solvency_score(data):
    score = 0
    b = BENCHMARKS["solvency"]

    if data["debt_to_equity"]:
        score += 1 if data["debt_to_equity"] <= b["debt_to_equity"] else b["debt_to_equity"] / data["debt_to_equity"]

    if data["current_ratio"]:
        score += min(data["current_ratio"] / b["current_ratio"], 1)

    return round(score / 2 * 100, 2)
