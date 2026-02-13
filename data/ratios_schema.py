# finsight/data/ratios_schema.py

RATIOS_SCHEMA = {

    # ───────── PROFITABILITY ─────────
    "roe": 0.0,
    "roa": 0.0,
    "net_margin": 0.0,
    "operating_margin": 0.0,

    # ───────── SOLVENCY / LIQUIDITY ─────────
    "debt_to_equity": 0.0,
    "current_ratio": 0.0,
    "interest_coverage": 0.0,

    # ───────── GROWTH (ABSOLUTE CONTRACT) ─────────
    "revenue_growth": 0.0,     # usado por growth_score
    "earnings_growth": 0.0,    # usado por growth_score
    "fcf_growth": 0.0,         # usado por growth_score

    # ───────── CAGR (si existen, se conservan) ─────────
    "revenue_cagr": 0.0,
    "earnings_cagr": 0.0,
    "fcf_cagr": 0.0,

    # ───────── VALUATION ─────────
    "pe": 0.0,
    "pb": 0.0,
    "ev_ebitda": 0.0,

    # ───────── RISK ─────────
    "beta": 1.0,
    "volatility": 0.2,
    "drawdown": -0.2,
}


