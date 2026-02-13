import requests
from .base import BaseProvider, ProviderError

ALPHA_API_KEY = "B6FRYG46N2707PCM"
BASE_URL = "https://www.alphavantage.co/query"


class AlphaVantageProvider(BaseProvider):
    name = "AlphaVantage"

    def fetch(self, ticker: str) -> dict:
        try:
            overview = requests.get(
                BASE_URL,
                params={
                    "function": "OVERVIEW",
                    "symbol": ticker,
                    "apikey": ALPHA_API_KEY,
                },
                timeout=10,
            ).json()

            if "Symbol" not in overview:
                raise ProviderError("Respuesta inválida Alpha")

            return {
                "source": self.name,
                "profile": overview,
                "ratios": overview,
                "growth": overview,
            }

        except Exception as e:
            raise ProviderError(str(e))
