# ---
# jupytext:
#   cell_metadata_filter: -all
#   formats: md:myst
#   text_representation:
#     extension: .md
#     format_name: myst
#     format_version: '0.9'
#     jupytext_version: 1.5.2
# kernelspec:
#   display_name: Python 3
#   language: python
#   name: python3
# ---

# Wyner-Ziv Quantization for Classification
# ==============================================
#
# ```{code-cell} python
# import xarray as xr
# import numpy as np
# import numpy.random as npr
# import matplotlib.pyplot as plt
# import pandas as pd
#
# plt.style.use('seaborn-darkgrid')
# plt.rcParams['figure.figsize'] = [16, 6]
# plt.rcParams['font.size'] = 14
# plt.rcParams['image.cmap'] = 'Dark2'
#
# DA = xr.DataArray
# ```
