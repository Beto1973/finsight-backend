from data.providers.fmp import FMPProvider
from data.providers.alpha_vantage import AlphaVantageProvider
from data.providers.polygon import PolygonProvider
from data.providers.base import ProviderError
from core.exceptions import InvalidTickerError


PROVIDERS = [
    FMPProvider(),
    AlphaVantageProvider(),
    PolygonProvider(),
]


def fetch_with_retry(ticker: str) -> dict:
    last_error = None

    for provider in PROVIDERS:
        try:
            return provider.fetch(ticker)
        except ProviderError as e:
            last_error = f"{provider.name}: {e}"

    raise InvalidTickerError(ticker=ticker, reason=str(last_error)
)


