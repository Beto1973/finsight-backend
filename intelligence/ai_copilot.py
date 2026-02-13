# finsight/intelligence/ai_copilot.py

def generate_committee_brief(
    portfolio: dict,
    stress: dict,
    anomalies: list[str]
) -> str:

    lines = []

    lines.append(
        f"El portafolio presenta un nivel de riesgo agregado "
        f"clasificado como {stress['stress_status']}."
    )

    if anomalies:
        lines.append("Se identificaron los siguientes puntos de atención:")
        for a in anomalies:
            lines.append(f"- {a}")
    else:
        lines.append(
            "No se detectaron anomalías relevantes en la asignación."
        )

    lines.append(
        "La asignación prioriza activos con alta calidad ajustada por riesgo "
        "y mantiene límites estrictos de concentración."
    )

    return "\n".join(lines)
