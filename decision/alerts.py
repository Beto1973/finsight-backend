def generate_alerts(ratios: dict, model_scores: dict) -> list[str]:
    alerts = []

    if ratios.get("de", 0) > 2:
        alerts.append("High leverage: Debt/Equity > 2")

    if ratios.get("revenue_growth", 0) < 0:
        alerts.append("Negative revenue growth")

    if ratios.get("earnings_growth", 0) < 0:
        alerts.append("Negative earnings growth")

    if ratios.get("pe", 0) > 35:
        alerts.append("Potential overvaluation (high P/E)")

    if model_scores.get("buffett", 0) >= 80:
        alerts.append("Strong economic moat (Buffett model)")

    if model_scores.get("graham", 0) < 50:
        alerts.append("Weak margin of safety (Graham model)")

    return alerts

