from core.scoring_engine import analyze_company

mock_ratios = {

    # ── PROFITABILITY ──
    "roe": 0.28,
    "roic": 0.22,
    "roa": 0.15,
    "net_margin": 0.21,

    # ── GROWTH (IMPORTANTE) ──
    "revenue_growth": 0.11,
    "earnings_growth": 0.14,   # ← CLAVE (NO eps_growth)
    "fcf_growth": 0.12,

    # ── SOLVENCY ──
    "debt_to_equity": 0.40,
    "current_ratio": 2.3,
    "interest_coverage": 8.0,

    # ── VALUATION ──
    "pe": 18.0,
    "pb": 2.1,
    "ev_ebitda": 12.0,

    # ── RISK ──
    "volatility": 0.18,
    "beta": 0.9,
    "drawdown": 0.22
}

result = analyze_company(mock_ratios)

print("\nRESULTADO FASE 3\n")
print("SCORE TOTAL:", round(result["score"], 2))
print("\nPILARES:")
for k, v in result["pillars"].items():
    print(f"{k}: {round(v, 2)}")

