def lloyd_max_optimization(enc, dec, X):
    pass




if __name__ == '__main__':
    from encoders import LocalEncoder
    from decoders import FusionDecoder
    import xarray as xr
    import numpy as np
    import matplotlib.pyplot as plt

    plt.style.use('seaborn-darkgrid')
    plt.rcParams['figure.figsize'] = [16, 9]
    plt.rcParams['font.size'] = 14
    plt.rcParams['image.cmap'] = 'Dark2'

    p = 16
    X = generate_2d_dataset(500, ρ=0.5)
    protos = sample(X, 'n', p).rename(n='p')
    q_indices = xr.DataArray(np.random.randint(2, size=p), dims='p')
    codebook = sample(X, 'n', 2).rename(n='m')

    enc = LocalEncoder(protos, q_indices)
    dec = FusionDecoder(codebook)

    enc = enc.optimize(X, dec)

    plt.scatter(*enc.protos.T, c=enc(enc.protos.rename(p='n')), marker='x', s=100)
    plt.scatter(*dec.codebook.T, c=enc(dec.codebook), marker='^', s=100)
    plt.scatter(*X.T, c=enc(X), alpha=0.3)

    # for i in range(3):
    #     enc = enc.optimize(X, dec)
    #     plt.subplot(3, 2, 2*i+1)
    #     print(enc)
    #     plt.scatter(*enc.protos.T, c=enc(enc.protos), marker='x', s=100)
    #     plt.scatter(*dec.codebook.T, c=enc(dec.codebook), marker='^', s=100)
    #     plt.scatter(*X.T, c=enc(X), alpha=0.1)

    #     dec = dec.optimize(X, enc)
    #     plt.subplot(3, 2, 2*i+2)
    #     plt.scatter(*dec.codebook.T, c=enc(dec.codebook), marker='^', s=100)
    #     plt.scatter(*X.T, c=enc(X), alpha=0.1)

    plt.show()
