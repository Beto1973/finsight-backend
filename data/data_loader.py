from data.cache import load_from_cache, save_to_cache
from data.provider import fetch_with_retry


def load_company_data(ticker: str, use_cache: bool = True) -> dict:
    ticker = ticker.upper()

    if use_cache:
        cached = load_from_cache(ticker)
        if cached:
            return cached

    data = fetch_with_retry(ticker)
    save_to_cache(ticker, data)
    return data

