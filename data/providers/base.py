from abc import ABC, abstractmethod


class ProviderError(Exception):
    pass


class BaseProvider(ABC):
    name: str

    @abstractmethod
    def fetch(self, ticker: str) -> dict:
        pass
