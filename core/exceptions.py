class InvalidTickerError(Exception):
    def __init__(self, ticker: str, reason: str = ""):
        self.ticker = ticker
        self.reason = reason
        super().__init__(f"Ticker inválido: {ticker}. {reason}")
