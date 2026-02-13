def evaluate_graham(data: dict) -> dict:
    score = 0
    checks = {}

    checks["pe"] = data.get("pe") is not None and data["pe"] < 15
    checks["pb"] = data.get("pb") is not None and data["pb"] < 1.5
    checks["current_ratio"] = data.get("current_ratio") is not None and data["current_ratio"] > 2
    checks["debt_assets"] = data.get("debt_assets") is not None and data["debt_assets"] < 0.5
    checks["eps"] = data.get("eps") is not None and data["eps"] > 0

    score = sum(checks.values())

    verdict = (
        "BUY" if score >= 4 else
        "HOLD" if score >= 2 else
        "AVOID"
    )

    return {
        "model": "Graham",
        "score": score,
        "max_score": 5,
        "verdict": verdict,
        "checks": checks
    }
