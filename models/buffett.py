def evaluate_buffett(data: dict) -> dict:
    score = 0
    checks = {}

    def ok(value, condition):
        return value is not None and condition(value)

    checks["roe"] = ok(data.get("roe"), lambda x: x > 0.15)
    checks["roic"] = ok(data.get("roic"), lambda x: x > 0.12)
    checks["net_margin"] = ok(data.get("net_margin"), lambda x: x > 0.10)
    checks["debt_equity"] = ok(data.get("debt_equity"), lambda x: x < 0.5)
    checks["fcf"] = ok(data.get("free_cash_flow"), lambda x: x > 0)
    checks["earnings_growth"] = ok(data.get("earnings_growth"), lambda x: x > 0)

    score = sum(checks.values())

    verdict = (
        "BUY" if score >= 5 else
        "HOLD" if score >= 3 else
        "AVOID"
    )

    return {
        "model": "Buffett",
        "score": score,
        "max_score": 6,
        "verdict": verdict,
        "checks": checks
    }
