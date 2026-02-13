from decision.rating import assign_rating

def investment_decision(score: float, risk_score: float) -> str:
    rating = assign_rating(score)

    if rating == "A" and risk_score >= 70:
        return "BUY"
    if rating == "B":
        return "HOLD"
    if rating == "C":
        return "WATCH"
    return "AVOID"
