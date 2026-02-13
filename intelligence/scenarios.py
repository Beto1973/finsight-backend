# finsight/intelligence/scenarios.py

SCENARIOS = {
    "base": {
        "market_shock": 0.00,
        "risk_multiplier": 1.0
    },
    "recession": {
        "market_shock": -0.25,
        "risk_multiplier": 1.4
    },
    "high_rates": {
        "market_shock": -0.15,
        "risk_multiplier": 1.2
    },
    "bull": {
        "market_shock": 0.20,
        "risk_multiplier": 0.9
    }
}


def apply_scenario(portfolio: dict, scenario: str) -> dict:
    s = SCENARIOS[scenario]

    stressed_allocations = []

    for a in portfolio["allocations"]:
        stressed_allocations.append({
            **a,
            "stressed_weight": round(
                a["weight"] * (1 + s["market_shock"]), 4
            ),
            "stressed_risk": round(
                a["risk"] * s["risk_multiplier"], 4
            )
        })

    return {
        "scenario": scenario,
        "allocations": stressed_allocations
    }
