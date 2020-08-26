Distributed Source Coding for Machine Learning
==============================================

## Compare one and two stage encoders

from dsc4ml.encoders import LocalEncoder, DistributedEncoder
from dsc4ml.decoders import FusionDecoder
import xarray as xr
import numpy as np
import numpy.random as npr
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('seaborn-darkgrid')
plt.rcParams['figure.figsize'] = [16, 6]
plt.rcParams['font.size'] = 14
plt.rcParams['image.cmap'] = 'Dark2'

DA = xr.DataArray

def generate_2d_dataset(n, ρ=0.0, sep=0.0):
    μ = [1, 0]
    Σ = [[1, ρ],
         [ρ, 1]]
    w = make_normal_unit_vector(2)
    X = DA(npr.multivariate_normal(μ, Σ, size=n), dims=['n', 'd'])
    y = np.sign(X @ w)
    X += sep*y*w
    return X, y


def sample(A, dim, size):
    i_sample = npr.randint(A[dim].size, size=size)
    return A[i_sample]


def total_loss(γ):
    def curry(A, B):
        w = make_normal_unit_vector(A.sizes['d'])
        mse = np.power(A - B, 2).sum('d')
        zero_one = (np.sign(A @ w) != np.sign(B @ w))
        return (1-γ)*mse + γ*zero_one
    return curry


def make_normal_unit_vector(d) -> '(d,)':
    w = np.append(-1, np.ones(d-1))
    w = w/np.sqrt(w @ w)
    return xr.DataArray(w, dims='d')


def plot_decision_boundary(X):
    p = [X.min(), X.max()]
    plt.plot(p, p, '--', alpha=0.25)

w = make_normal_unit_vector(2)

### One-stage (prototypes $=$ codebook)

for γ in [0, 0.1, 0.9, 1.0]:
    npr.seed(0)

    X, _ = generate_2d_dataset(500, ρ=0.5, sep=0.15)
    codebook = sample(X, 'n', 2).rename(n='m')
    protos = codebook.rename(m='p')
    q_indices = DA(np.arange(2), dims='p')

    enc = LocalEncoder(protos, q_indices, rate=2)
    dec = FusionDecoder(codebook)

    losses = list()
    Z, _ = generate_2d_dataset(500, ρ=0.5, sep=0.15)
    for i in range(10):
        dec = dec.optimize(X, enc, γ, w)
        enc = (LocalEncoder(dec.codebook.rename(m='p'), q_indices, 2)
               .optimize(X, dec, total_loss(γ)))
        losses.append({'Train': total_loss(γ)(X, dec(enc(X))).mean().item(),
                       'Test': total_loss(γ)(Z, dec(enc(Z))).mean().item()})

    losses = pd.DataFrame(losses)

    plt.subplot(1, 2, 1)
    plt.scatter(*enc.protos.T, c=enc(enc.protos.rename(p='n')), marker='x', s=100)
    plt.scatter(*dec.codebook.T, c=enc(dec.codebook), marker='^', s=100)
    plt.scatter(*X.T, c=enc(X), alpha=0.15)
    plot_decision_boundary(X)

    ax = plt.subplot(1, 2, 2)
    losses.plot(ax=ax, style='o--')
    plt.title(f'Total loss ($\gamma = {γ:.2f}$)')
    plt.show()
    print(dec)

### Two-stage (prototypes $\neq$ codebook)

for γ in [0, 0.1, 0.9, 1.0]:
    npr.seed(0)

    p = 16
    X, _ = generate_2d_dataset(300, ρ=0.5, sep=0.2)
    protos = sample(X, 'n', p).rename(n='p')
    q_indices = DA(npr.randint(2, size=p), dims='p')
    codebook = sample(X, 'n', 2).rename(n='m')

    enc = LocalEncoder(protos, q_indices, rate=2)
    dec = FusionDecoder(codebook)

    losses = list()
    Z, _ = generate_2d_dataset(300, ρ=0.5, sep=0.2)
    for i in range(10):
        dec = dec.optimize(X, enc, γ, w)
        enc = enc.optimize(X, dec, total_loss(γ))
        losses.append({'Train': total_loss(γ)(X, dec(enc(X))).mean().item(),
                       'Test': total_loss(γ)(Z, dec(enc(Z))).mean().item()})

    losses = pd.DataFrame(losses)

    plt.subplot(1, 2, 1)
    plt.scatter(*enc.protos.T, c=enc(enc.protos.rename(p='n')), marker='x', s=100)
    plt.scatter(*dec.codebook.T, c=enc(dec.codebook), marker='^', s=100)
    plt.scatter(*X.T, c=enc(X), alpha=0.15)
    plot_decision_boundary(X)

    ax = plt.subplot(1, 2, 2)
    losses.plot(ax=ax, style='o--')
    plt.title(f'Total loss ($\gamma = {γ:.2f}$)')
    plt.show()
    print(dec)

## Two-stage Distributed Encoders

npr.seed(0)
for γ in [0, 0.1, 0.9, 1.0]:

    # Untreated corner cases (both will break the code):
    # - If p is too large, there will be proto-regions without points.
    # - If rate_exp is too large, some integer will be proto-region-less
    p = [10, 5]
    rate_exp = [2, 2]

    X, _ = generate_2d_dataset(1_000, ρ=0.5, sep=0.2)
    encoders = [
        LocalEncoder(DA(np.linspace(-1.5, 1.5, p[0]), dims='p').expand_dims(d=1),
                     DA(npr.randint(rate_exp[0], size=p[0]), dims='p'),
                     rate_exp[0]),

        LocalEncoder(DA(np.linspace(-1.5, 1.5, p[1]), dims='p').expand_dims(d=1),
                     DA(npr.randint(rate_exp[1], size=p[1]), dims='p'),
                     rate_exp[1])
    ]

    enc = DistributedEncoder(encoders)
    dec = FusionDecoder.init_from_encoder(X, enc, γ, w)

    losses = list()
    Z, _ = generate_2d_dataset(1_000, ρ=0.5, sep=0.2)
    for i in range(10):
        dec = dec.optimize(X, enc, γ, w)
        enc = enc.optimize(X, dec, total_loss(γ))
        losses.append({'Train': total_loss(γ)(X, dec(enc(X))).mean().item(),
                       'Test': total_loss(γ)(Z, dec(enc(Z))).mean().item()})

    losses = pd.DataFrame(losses)

    plt.subplot(1, 2, 1)
    plt.scatter(*dec.codebook.T, c=enc(dec.codebook), marker='^', s=100)
    plt.scatter(*X.T, c=enc(X), alpha=0.15)
    plt.xticks(enc[0].boundaries.round(2), '')
    plt.yticks(enc[1].boundaries.round(2), '')
    plot_decision_boundary(X)

    ax = plt.subplot(1, 2, 2)
    losses.plot(ax=ax, style='o--')
    plt.title(f'Total loss ($\gamma = {γ:.2f}$)')
    plt.show()
    print(dec)

```{toctree}
:hidden:
:titlesonly:


.pytest_cache/README
dsc4ml/decoders
```