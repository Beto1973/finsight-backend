# finsight/core/explanation_engine.py

def _explain_score_level(value: float, high=0.75, mid=0.5):
    if value >= high:
        return "fuerte"
    elif value >= mid:
        return "aceptable"
    return "débil"


def _pillar_explanation(name: str, score: float) -> str:
    level = _explain_score_level(score)

    explanations = {
        "profitability": {
            "fuerte": "La compañía muestra una rentabilidad sólida, con retornos consistentes sobre el capital.",
            "aceptable": "La rentabilidad es razonable, aunque sin una ventaja clara frente a pares del mercado.",
            "débil": "La rentabilidad es limitada y no demuestra retornos atractivos sobre el capital invertido."
        },
        "growth": {
            "fuerte": "El crecimiento es robusto, con expansión sostenida en ingresos y resultados.",
            "aceptable": "El crecimiento es moderado y acompaña al mercado.",
            "débil": "El crecimiento es débil o inconsistente en el tiempo."
        },
        "solvency": {
            "fuerte": "La estructura financiera es sólida, con bajo apalancamiento y buena cobertura.",
            "aceptable": "La solvencia es adecuada, aunque con cierto nivel de dependencia del endeudamiento.",
            "débil": "La solvencia es frágil y presenta riesgos financieros relevantes."
        },
        "valuation": {
            "fuerte": "La valuación resulta atractiva en relación con sus fundamentales.",
            "aceptable": "La acción cotiza en niveles razonables frente a su valor intrínseco.",
            "débil": "La valuación es exigente y deja poco margen de seguridad."
        },
        "risk": {
            "fuerte": "El perfil de riesgo es bajo, con volatilidad y exposición controladas.",
            "aceptable": "El riesgo es moderado y coherente con el mercado.",
            "débil": "El activo presenta un perfil de riesgo elevado."
        }
    }

    return explanations.get(name, {}).get(level, "")


def _model_explanation(name: str, score: float) -> str:
    level = _explain_score_level(score)

    texts = {
        "buffett": {
            "fuerte": "Según el enfoque de Warren Buffett, la empresa presenta ventajas competitivas sostenibles y retornos consistentes.",
            "aceptable": "Bajo el enfoque Buffett, el negocio es razonable pero sin un moat claramente definido.",
            "débil": "El enfoque Buffett no identifica una ventaja competitiva clara ni retornos atractivos."
        },
        "graham": {
            "fuerte": "Desde la óptica de Benjamin Graham, existe margen de seguridad y fundamentos sólidos.",
            "aceptable": "El enfoque Graham muestra fundamentos correctos, aunque con margen de seguridad limitado.",
            "débil": "El enfoque Graham no identifica una valuación suficientemente conservadora."
        },
        "lynch": {
            "fuerte": "Bajo el enfoque de Peter Lynch, la compañía combina crecimiento atractivo con valuación razonable.",
            "aceptable": "Según Lynch, el crecimiento es aceptable pero sin un atractivo diferencial.",
            "débil": "El enfoque Lynch refleja bajo crecimiento o valuación poco atractiva."
        }
    }

    return texts.get(name, {}).get(level, "")


def generate_explanation(result: dict) -> dict:
    pillars = result.get("pillars", {})
    models = result.get("models", {})
    alerts = result.get("alerts", [])
    decision = result.get("decision", "")
    rating = result.get("rating", "")
    score = result.get("score", 0)

    pillar_texts = {
        name: _pillar_explanation(name, value)
        for name, value in pillars.items()
    }

    model_texts = {
        name: _model_explanation(name, value)
        for name, value in models.items()
    }

    summary = (
        f"La compañía obtiene un score global de {round(score * 100, 1)}%, "
        f"con calificación {rating}. "
        f"La recomendación del sistema es: {decision}."
    )

    decision_rationale = (
        "La decisión se fundamenta en la combinación de métricas financieras, "
        "modelos de inversión clásicos y alertas de riesgo identificadas."
    )

    return {
        "summary": summary,
        "pillars": pillar_texts,
        "models": model_texts,
        "alerts": alerts,
        "decision_rationale": decision_rationale
    }


