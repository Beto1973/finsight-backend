# finsight/portfolio/allocator.py

MAX_WEIGHT = 0.25
MIN_WEIGHT = 0.02


def allocate_weights(assets: list[dict]) -> list[dict]:
    """
    assets: [
        {
            "ticker": str,
            "score": float,
            "risk": float,
            "decision": str
        }
    ]
    """

    valid_assets = [
        a for a in assets
        if a["decision"] == "BUY"
    ]

    if not valid_assets:
        return []

    for a in valid_assets:
        a["adjusted_score"] = a["score"] * (1 - a["risk"])

    total = sum(a["adjusted_score"] for a in valid_assets)

    for a in valid_assets:
        raw_weight = a["adjusted_score"] / total if total > 0 else 0
        a["weight"] = min(MAX_WEIGHT, raw_weight)

    # Normalización final
    norm = sum(a["weight"] for a in valid_assets)

    for a in valid_assets:
        a["weight"] = round(a["weight"] / norm, 4) if norm > 0 else 0

        if a["weight"] < MIN_WEIGHT:
            a["weight"] = 0

    return valid_assets
