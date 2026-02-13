# finsight/core/scoring_engine.py

from scoring.profitability import profitability_score
from scoring.solvency import solvency_score
from scoring.growth import growth_score
from scoring.valuation import valuation_score
from scoring.risk import risk_score
from scoring.total import calculate_total_score

from scoring.buffett import buffett_score
from scoring.graham import graham_score
from scoring.lynch import lynch_score


def analyze_company(ratios: dict) -> dict:
    profitability = profitability_score(ratios)
    solvency = solvency_score(ratios)
    growth = growth_score(ratios)
    valuation = valuation_score(ratios)
    risk = risk_score(ratios)

    buffett = buffett_score(ratios)
    graham = graham_score(ratios)
    lynch = lynch_score(ratios)

    total = calculate_total_score(
        profitability=profitability,
        solvency=solvency,
        growth=growth,
        valuation=valuation,
        risk=risk,
        buffett=buffett,
        graham=graham,
        lynch=lynch
    )

    return {
        "score": total,
        "pillars": {
            "profitability": profitability,
            "solvency": solvency,
            "growth": growth,
            "valuation": valuation,
            "risk": risk,
            "buffett": buffett,
            "graham": graham,
            "lynch": lynch
        }
    }



