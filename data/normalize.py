from data.providers.yahoo_mapper import normalize_yahoo
from data.providers.fmp_mapper import normalize_fmp
from data.providers.alpha_vantage_mapper import normalize_alpha_vantage
from data.providers.polygon_mapper import normalize_polygon


def normalize_financials(raw: dict, provider: str, ticker: str) -> dict:
    provider = provider.lower()

    if provider == "yahoo":
        return normalize_yahoo(raw, ticker)

    if provider == "fmp":
        return normalize_fmp(raw, ticker)

    if provider == "alpha_vantage":
        return normalize_alpha_vantage(raw, ticker)

    if provider == "polygon":
        return normalize_polygon(raw, ticker)

    if provider == "mock":
        return raw  # mock ya viene normalizado

    raise ValueError(f"Proveedor no soportado: {provider}")

