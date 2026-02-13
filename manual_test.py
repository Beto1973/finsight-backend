# finsight/manual_test.py
from data.data_loader import load_company_data
from data.ratios import calculate_ratios

if __name__ == "__main__":
    ticker = "AAPL"

    raw_data = load_company_data(ticker)
    ratios = calculate_ratios(raw_data)

    print(f"\nRATIOS CALCULADOS PARA {ticker}:")
    for k, v in ratios.items():
        print(f"{k}: {v}")

