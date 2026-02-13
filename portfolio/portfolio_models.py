# finsight/portfolio/portfolio_models.py

from dataclasses import dataclass

@dataclass
class AssetAllocation:
    ticker: str
    score: float
    risk: float
    adjusted_score: float
    weight: float
