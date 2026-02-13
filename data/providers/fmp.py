import requests
from .base import BaseProvider, ProviderError

FMP_API_KEY = "gwFFyVIecvxyHFkeCGDHDUP814OwMSwP"
BASE_URL = "https://financialmodelingprep.com/api/v3"


class FMPProvider(BaseProvider):
    name = "FinancialModelingPrep"

    def fetch(self, ticker: str) -> dict:
        try:
            profile = requests.get(
                f"{BASE_URL}/profile/{ticker}",
                params={"apikey": FMP_API_KEY},
                timeout=10,
            ).json()

            ratios = requests.get(
                f"{BASE_URL}/ratios/{ticker}",
                params={"apikey": FMP_API_KEY},
                timeout=10,
            ).json()

            growth = requests.get(
                f"{BASE_URL}/financial-growth/{ticker}",
                params={"apikey": FMP_API_KEY},
                timeout=10,
            ).json()

            if not profile or not ratios:
                raise ProviderError("Respuesta vacía FMP")

            return {
                "source": self.name,
                "profile": profile[0],
                "ratios": ratios[0],
                "growth": growth[0] if growth else {},
            }

        except Exception as e:
            raise ProviderError(str(e))
