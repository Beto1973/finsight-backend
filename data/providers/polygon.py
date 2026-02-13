import requests
from .base import BaseProvider, ProviderError

POLYGON_API_KEY = "mVhOm3CPHgzU1kFg9Hjkl_Pxl4_fAplA"
BASE_URL = "https://api.polygon.io"


class PolygonProvider(BaseProvider):
    name = "Polygon"

    def fetch(self, ticker: str) -> dict:
        try:
            financials = requests.get(
                f"{BASE_URL}/vX/reference/financials",
                params={
                    "ticker": ticker,
                    "apiKey": POLYGON_API_KEY,
                },
                timeout=10,
            ).json()

            if "results" not in financials:
                raise ProviderError("Respuesta inválida Polygon")

            return {
                "source": self.name,
                "profile": financials["results"][0],
                "ratios": financials["results"][0],
                "growth": financials["results"][0],
            }

        except Exception as e:
            raise ProviderError(str(e))
