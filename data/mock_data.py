
from data.ratios_schema import RATIOS_SCHEMA

def get_mock_ratios() -> dict:
    return {
        **RATIOS_SCHEMA,
        "roe": 0.22,
        "roa": 0.14,
        "net_margin": 0.21,
        "debt_to_equity": 0.4,
        "current_ratio": 1.9,
        "interest_coverage": 9,
        "revenue_cagr": 0.08,
        "eps_cagr": 0.1,
        "fcf_cagr": 0.09,
        "pe": 18,
        "pb": 4,
        "ev_ebitda": 11,
        "beta": 0.9,
        "volatility": 0.18,
        "drawdown": -0.25
    }

def load_mock_company_data(ticker: str) -> dict:
    """
    Datos mockeados realistas para desarrollo, testing y demos.
    No depende de proveedores externos.
    """
    mock_database = {
        "AAPL": {
            "ticker": "AAPL",
            "currency": "USD",
            "revenue": 383_000_000_000,
            "netIncome": 97_000_000_000,
            "equity": 74_000_000_000,
            "totalAssets": 352_000_000_000,
            "totalDebt": 110_000_000_000,
            "currentAssets": 143_000_000_000,
            "currentLiabilities": 145_000_000_000,
            "operatingIncome": 114_000_000_000,
            "interestExpense": 3_000_000_000,

            # Crecimiento
            "revenueCAGR": 0.08,
            "epsCAGR": 0.10,
            "fcfCAGR": 0.09,

            # Valoración
            "trailingPE": 28.5,
            "priceToBook": 35.0,
            "enterpriseToEbitda": 22.0,

            # Riesgo
            "beta": 1.25,
            "volatility": 0.30,
            "maxDrawdown": -0.32,

            "source": "mock"
        },

        "MSFT": {
            "ticker": "MSFT",
            "currency": "USD",
            "revenue": 211_000_000_000,
            "netIncome": 72_000_000_000,
            "equity": 166_000_000_000,
            "totalAssets": 411_000_000_000,
            "totalDebt": 78_000_000_000,
            "currentAssets": 184_000_000_000,
            "currentLiabilities": 104_000_000_000,
            "operatingIncome": 89_000_000_000,
            "interestExpense": 2_500_000_000,

            "revenueCAGR": 0.11,
            "epsCAGR": 0.13,
            "fcfCAGR": 0.12,

            "trailingPE": 34.0,
            "priceToBook": 11.5,
            "enterpriseToEbitda": 25.0,

            "beta": 0.95,
            "volatility": 0.24,
            "maxDrawdown": -0.28,

            "source": "mock"
        }
    }

    if ticker not in mock_database:
        raise ValueError(f"Ticker mock no disponible: {ticker}")

    return mock_database[ticker]
