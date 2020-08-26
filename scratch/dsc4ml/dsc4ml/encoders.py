from .core import Encoder
import numpy as np
import xarray as xr


class LocalEncoder(Encoder):
    def __init__(self, protos, q_indices, rate):
        """
        Args:
            protos (DataArray): p, d 
            q_incides (DataArray): p
        """
        self.protos = protos
        self.rate = rate
        self.q_indices = q_indices

    def assign_to_proto(self, X):
        return (np.power(X - self.protos, 2)
                  .sum('d')
                  .argmin('p'))

    def encode(self, X):
        i = self.assign_to_proto(X)
        return self.q_indices.sel(p=i)

    def optimize(self, X, dec, loss_func):
        P = self.assign_to_proto(X)
        q_indices = (loss_func(X, dec.codebook)
                     .groupby(P)
                     .mean()
                     .rename(group='p')
                     .argmin('m')
                     .drop('p'))
        return type(self)(self.protos, q_indices, self.rate)

    def __repr__(self):
        proto_str = ('proto:\t\t' 
                     + '\n\t\t'.join(self.protos.__repr__().split('\n'))
                     + '\n')
        q_indices_str = ('q_indices:\t' 
                         + '\n\t\t'.join(self.q_indices.__repr__().split('\n'))
                         + '\n')
        return proto_str + q_indices_str

    @property
    def boundaries(self):
        return ((self.protos + self.protos.shift(p=1))
                     .dropna(dim='p')
                     .rename(p='b')
                     .sel(d=0))/2

    def copy(self):
        return type(self)(protos=self.protos.copy(),
                          q_indices=self.q_indices.copy(),
                          rate=self.rate)


class DistributedEncoder(Encoder):
    def __init__(self, encoders):
        """
        Args:
            encoders (List[Encoder])
        """
        self.encoders = encoders
        self.rates = [e.rate for e in encoders]
        self.rate = np.prod(self.rates)

    def encode(self, X):
        Q = [enc(X.sel(d=[i]))
             for i, enc in enumerate(self.encoders)]
        return xr.concat(Q, dim='d').T.pipe(self.flatten)

    def flatten(self, Q):
        Q_flat = np.ravel_multi_index(Q.T, dims=self.rates)
        return xr.DataArray(Q_flat, dims=['n'])

    def optimize(self, X, dec, loss_func):
        # this implementation assumes that the loss of each proto-region
        # does not depend on any other proto-region, except itself, for any
        # LocalEncoder

        def make_q_indices(enc):
            return [xr.ones_like(enc.q_indices)*i
                    for i in range(enc.rate)]

        enc = self.copy()
        for i, e in enumerate(self):
            Xi = X.sel(d=[i])
            P = e.assign_to_proto(Xi)
            losses = list()
            for q_indices_const in make_q_indices(e):
                enc[i] = type(e)(e.protos, q_indices_const, e.rate)
                loss = (loss_func(X, dec(enc(X)))
                        .groupby(P)
                        .mean()
                        .rename(group='p')
                        .drop('p'))
                losses.append(loss)
            losses = xr.concat(losses, dim='opt').T
            q_indices = losses.argmin('opt')
            enc[i] = type(e)(e.protos, q_indices, e.rate)
        return enc

    def __getitem__(self, i):
        return self.encoders[i]

    def __setitem__(self, i, x):
        self.encoders[i] = x

    @property
    def boundaries(self):
        return [e.boundaries for e in self.encoders]

    def assign_to_proto(self, X):
        return [e.assign_to_proto(X.sel(d=[i]))
                for i, e in enumerate(self.encoders)]

    def copy(self):
        return type(self)([e.copy() for e in self.encoders])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
