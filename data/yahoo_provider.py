# finsight/data/yahoo_provider.py
import yfinance as yf


def fetch_from_yahoo(ticker: str) -> dict:
    t = yf.Ticker(ticker)

    info = t.info
    financials = t.financials
    balance = t.balance_sheet
    cashflow = t.cashflow
    history = t.history(period="5y")

    if not info:
        raise RuntimeError("Yahoo devolvió info vacía")

    return {
        "info": info,
        "financials": financials,
        "balance": balance,
        "cashflow": cashflow,
        "history": history,
    }
