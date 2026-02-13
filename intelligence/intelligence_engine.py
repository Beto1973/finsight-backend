# finsight/intelligence/intelligence_engine.py

from intelligence.scenarios import apply_scenario
from intelligence.stress_test import stress_test_portfolio
from intelligence.anomaly_detector import detect_anomalies
from intelligence.ai_copilot import generate_committee_brief


def run_intelligence_layer(portfolio: dict) -> dict:
    stress = stress_test_portfolio(portfolio)
    anomalies = detect_anomalies(portfolio["allocations"])

    explanation = generate_committee_brief(
        portfolio=portfolio,
        stress=stress,
        anomalies=anomalies
    )

    return {
        "stress": stress,
        "anomalies": anomalies,
        "committee_brief": explanation
    }
