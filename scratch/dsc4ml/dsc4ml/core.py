from abc import ABC, abstractmethod


class Encoder(ABC):
    @abstractmethod
    def encode(self, X):
        """
        Args:
            X (DataArray): 'N', 'd'

        Returns:
            DataArray: 'N'
        """

    def __call__(self, *args, **kwargs):
        return self.encode(*args, **kwargs)


class Decoder(ABC):
    @abstractmethod
    def decode(self, Q):
        """
        Args:
            Q (DataArray): N
        """

    def __call__(self, *args, **kwargs):
        return self.decode(*args, **kwargs)
