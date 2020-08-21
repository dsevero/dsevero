from .core import Decoder
import numpy as np
import xarray as xr


class FusionDecoder(Decoder):
    def __init__(self, codebook):
        """
        Args:
            codebook (DataArray): m, d
        """
        self.codebook = codebook

    def decode(self, Q):
        return self.codebook[Q]


    def optimize(self, X, enc):
        Q = enc(X)
        codebook = (X.groupby(Q)
                     .mean()
                     .rename(group='m'))
        return type(self)(codebook)

    def __repr__(self):
        return ('codebook:\t'
                + '\n\t\t'.join(self.codebook.__repr__().split('\n'))
                + '\n')

    @classmethod
    def init_from_encoder(cls, X, enc):
        return cls(None).optimize(X, enc)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
