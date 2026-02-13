def calculate_total_score(
    profitability: float,
    growth: float,
    solvency: float,
    valuation: float,
    risk: float,
    buffett: float = 0.0,
    graham: float = 0.0,
    lynch: float = 0.0
) -> float:
    """
    Calcula el score total del activo.
    Extendido para integrar modelos Buffett, Graham y Lynch
    sin romper compatibilidad previa.
    """

    base_score = (
        profitability * 0.25 +
        growth * 0.20 +
        solvency * 0.20 +
        valuation * 0.20 +
        risk * 0.15
    )

    model_score = (
        buffett * 0.05 +
        graham * 0.05 +
        lynch * 0.05
    )

    total = base_score + model_score

    return round(total, 2)


