# finsight/intelligence/anomaly_detector.py

def detect_anomalies(allocations: list[dict]) -> list[str]:
    alerts = []

    for a in allocations:
        if a["weight"] > 0.25:
            alerts.append(
                f"Alta concentración en {a['ticker']} ({a['weight']:.0%})"
            )

        if a["risk"] > 0.6 and a["weight"] > 0.10:
            alerts.append(
                f"Riesgo elevado en {a['ticker']} con peso significativo"
            )

    return alerts
