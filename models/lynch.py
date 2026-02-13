def evaluate_lynch(data: dict) -> dict:
    score = 0
    checks = {}

    checks["revenue_growth"] = data.get("revenue_growth") is not None and data["revenue_growth"] > 0.10
    checks["earnings_growth"] = data.get("earnings_growth") is not None and data["earnings_growth"] > 0.10
    checks["peg"] = data.get("peg") is not None and data["peg"] < 1.5
    checks["debt_equity"] = data.get("debt_equity") is not None and data["debt_equity"] < 1
    checks["roe"] = data.get("roe") is not None and data["roe"] > 0

    score = sum(checks.values())

    verdict = (
        "BUY" if score >= 4 else
        "HOLD" if score >= 2 else
        "AVOID"
    )

    return {
        "model": "Lynch",
        "score": score,
        "max_score": 5,
        "verdict": verdict,
        "checks": checks
    }
