# finsight/data/cache.py
import pickle
from pathlib import Path
from datetime import datetime, timedelta

CACHE_DIR = Path("cache")
CACHE_DIR.mkdir(exist_ok=True)

TTL_HOURS = 24  # tiempo de vida del cache


def _cache_path(ticker: str) -> Path:
    return CACHE_DIR / f"{ticker.upper()}.pkl"


def load_from_cache(ticker: str):
    path = _cache_path(ticker)
    if not path.exists():
        return None

    with open(path, "rb") as f:
        payload = pickle.load(f)

    timestamp = payload.get("_cached_at")
    if not timestamp:
        return None

    if datetime.utcnow() - timestamp > timedelta(hours=TTL_HOURS):
        return None

    return payload["data"]


def save_to_cache(ticker: str, data: dict):
    path = _cache_path(ticker)
    payload = {
        "_cached_at": datetime.utcnow(),
        "data": data
    }
    with open(path, "wb") as f:
        pickle.dump(payload, f)
