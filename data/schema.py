# finsight/data/schema.py

from typing import Optional, Dict


class NormalizedFinancials(dict):
    """
    Modelo financiero canónico.
    Todos los providers deben mapear a este esquema.
    """

    # --- Identidad ---
    ticker: str
    currency: Optional[str]

    # --- Income Statement ---
    revenue: Optional[float]
    net_income: Optional[float]
    operating_income: Optional[float]

    # --- Balance Sheet ---
    total_assets: Optional[float]
    total_liabilities: Optional[float]
    equity: Optional[float]
    debt: Optional[float]
    cash: Optional[float]
    current_assets: Optional[float]
    current_liabilities: Optional[float]

    # --- Cash Flow ---
    operating_cash_flow: Optional[float]
    free_cash_flow: Optional[float]

    # --- Market Data ---
    market_cap: Optional[float]
    price: Optional[float]
    shares_outstanding: Optional[float]

    # --- Valuation ---
    pe: Optional[float]
    pb: Optional[float]
    ev_ebitda: Optional[float]

    # --- Growth ---
    revenue_growth: Optional[float]
    earnings_growth: Optional[float]
    fcf_growth: Optional[float]

    # --- Risk ---
    beta: Optional[float]
    volatility: Optional[float]
    max_drawdown: Optional[float]

    # --- Metadata ---
    provider: str
    data_quality_score: float
