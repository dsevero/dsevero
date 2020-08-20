from core import Decoder
import numpy as np
import xarray as xr


class FusionDecoder(Decoder):
    def __init__(self, codebook):
        """
        Args:
            codebook (DataArray): 'M', 'd'
        """
        self.codebook = codebook
        self.d = codebook.sizes['d']

    def decode(self, Q_flat):
        return self.codebook[Q_flat]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
