from core.scoring_engine import analyze_company
from data.mock_data import get_mock_ratios
from decision.rating import assign_rating
from decision.decision_engine import investment_decision
from decision.alerts import generate_alerts

# Mock ratios
mock_ratios = get_mock_ratios()

# Scoring
result = analyze_company(mock_ratios)

# Decision layer
rating = assign_rating(result["score"])

decision = investment_decision(
    score=result["score"],
    risk_score=result["pillars"]["risk"]
)

alerts = generate_alerts(
    mock_ratios,
    result["pillars"]
)

print("SCORE:", result["score"])
print("RATING:", rating)
print("DECISION:", decision)
print("ALERTS:", alerts)

