from core import Encoder
import numpy as np
import xarray as xr


class LocalEncoder(Encoder):
    def __init__(self, protos, q_indices):
        """
        Args:
            protos (DataArray): 'p', 'd'
            q_incides (DataArray): 'p'
        """
        self.protos = protos
        self.q_incides = q_indices
        self.rate_exp = q_indices.max().item() + 1

    def encode(self, X):
        i = (np.power(X - self.protos, 2)
               .sum('d')
               .argmin('p'))
        return self.q_incides[i]


class DistributedEncoder(Encoder):
    """
    >>> import xarray as xr
    >>> enc1 = LocalEncoder(xr.DataArray([[0.1, 0.5, 0.3]], dims=['d', 'p']),
    ...                     xr.DataArray([0, 1, 2], dims=['p']))
    >>> enc1.rate_exp
    3
    >>> enc2 = LocalEncoder(xr.DataArray([[0.2, 0.4]], dims=['d', 'p']),
    ...                     xr.DataArray([0, 1], dims=['p']))
    >>> enc2.rate_exp
    2
    >>> X = xr.DataArray([[0.2, 0.25],
    ...                   [0.4,  0.4],
    ...                   [0.0,  0.6]],
    ...                  dims=['n', 'd'])
    >>> enc_dist = DistributedEncoder([enc1, enc2])
    >>> enc_dist.rate_exps
    [3, 2]
    >>> enc_dist(X)
    <xarray.DataArray (n: 3, d: 2)>
    array([[2, 0],
           [1, 1],
           [0, 1]])
    Dimensions without coordinates: n, d
    >>> enc_dist(X, flatten=True)
    <xarray.DataArray (n: 3)>
    array([4, 3, 1])
    Dimensions without coordinates: n
    """

    def __init__(self, encoders):
        """
        Args:
            encoders (List[Encoder])
        """
        self.encoders = encoders
        self.rate_exps = [e.rate_exp for e in encoders]

    def encode(self, X, flatten=False):
        Q = [enc(X.sel(d=[i]))
             for i, enc in enumerate(self.encoders)]
        Q = xr.concat(Q, dim='d').T
        if flatten:
            Q = self.flatten(Q)
        return Q

    def flatten(self, Q):
        Q_flat = np.ravel_multi_index(Q.T, dims=self.rate_exps)
        return xr.DataArray(Q_flat, dims=['n'])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
