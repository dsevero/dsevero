from .core import Decoder
import numpy as np
import xarray as xr
import numpy.random as npr


class FusionDecoder(Decoder):
    def __init__(self, codebook):
        """
        Args:
            codebook (DataArray): m, d
        """
        self.codebook = codebook
        self.m = codebook.sizes['m'] if codebook is not None else 0

    def decode(self, Q):
        return self.codebook[Q]

    def optimize(self, X, enc, γ, w):
        Q = enc(X)
        codebook = (X.groupby(Q)
                     .mean()
                     .rename(group='m'))

        if w is not None and γ > 0:
            Δ = -(codebook @ w)*w*(1 + 1e-3)
            codebook = xr.concat((codebook + Δ, codebook), dim='Δ')
            yhat = np.sign(codebook @ w)
            y = np.sign(X @ w)
            loss = (1-γ)*np.power(X - codebook, 2).sum('d') + γ*(y != y)
            codebook = codebook.sel(Δ=loss.mean('n').argmin('Δ'))

        codebook = self.complete_codebook(codebook, X)
        return type(self)(codebook)

    def __repr__(self):
        return ('codebook:\t'
                + '\n\t\t'.join(self.codebook.__repr__().split('\n'))
                + '\n')

    def complete_codebook(self, codebook, X):
        Δm = self.m - codebook.sizes['m']
        if Δm > 0:
            i = npr.randint(X.sizes['n'], size=Δm)
            sampled_codewords = X[i].rename(n='m')
            codebook = xr.concat((sampled_codewords, codebook.drop('m')),
                                 dim='m')
            codebook = codebook.sel(m=npr.permutation(codebook.sizes['m']))
        return codebook


    @classmethod
    def init_from_encoder(cls, X, enc, γ, w):
        dec = cls(None).optimize(X, enc, γ, w)
        dec.m = np.prod(enc.rates)
        return dec.optimize(X, enc, γ, w)



if __name__ == '__main__':
    import doctest
    doctest.testmod()
