import numpy as np
from data.ratios_schema import RATIOS_SCHEMA


def safe_div(a, b):
    if a in (None, 0) or b in (None, 0):
        return None
    return a / b


def calculate_ratios(data: dict) -> dict:
    """
    Calcula ratios financieros de forma defensiva.
    Soporta datos parciales o fallback.
    """

    # --------------------
    # Rentabilidad
    # --------------------
    roe = safe_div(data.get("netIncome"), data.get("equity"))
    roa = safe_div(data.get("netIncome"), data.get("totalAssets"))
    net_margin = safe_div(data.get("netIncome"), data.get("revenue"))

    # --------------------
    # Solvencia
    # --------------------
    de = safe_div(data.get("totalDebt"), data.get("equity"))
    current_ratio = safe_div(
        data.get("currentAssets"),
        data.get("currentLiabilities")
    )
    interest_coverage = safe_div(
        data.get("operatingIncome"),
        data.get("interestExpense")
    )

    # --------------------
    # Crecimiento
    # --------------------
    revenue_cagr = data.get("revenueCAGR")
    eps_cagr = data.get("epsCAGR")
    fcf_cagr = data.get("fcfCAGR")

    # --------------------
    # Valoración
    # --------------------
    pe = data.get("trailingPE")
    pb = data.get("priceToBook")
    ev_ebitda = data.get("enterpriseToEbitda")

    # --------------------
    # Riesgo
    # --------------------
    volatility = data.get("volatility")
    beta = data.get("beta")
    drawdown = data.get("maxDrawdown")

    raw_ratios = {
        "roe": roe,
        "roa": roa,
        "net_margin": net_margin,

        # 🔒 contrato explícito
        "debt_to_equity": de,
        "current_ratio": current_ratio,
        "interest_coverage": interest_coverage,

        "revenue_cagr": revenue_cagr,
        "revenue_growth": revenue_cagr,
        "eps_cagr": eps_cagr,
        "fcf_cagr": fcf_cagr,

        "pe": pe,
        "pb": pb,
        "ev_ebitda": ev_ebitda,

        "volatility": volatility,
        "beta": beta,
        "drawdown": drawdown,
    }

    # --------------------
    # Normalización FINAL (no altera lógica)
    # --------------------
    normalized = RATIOS_SCHEMA.copy()
    for k, v in raw_ratios.items():
        if v is not None:
            normalized[k] = v

    return normalized
