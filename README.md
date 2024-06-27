
**Research Engineer**

**Meta - Fundamental AI Research (FAIR) Labs**

Originally, I am from Florianópolis (Brazil) but I've lived in New Jersey, Orlando, Toronto (now), São Paulo, as well as other smaller cities in the south of Brazil.
I spent 2022 at [Google AI](https://ai.google/) with [Lucas Theis](http://theis.io/) and [Johannes Ballé](https://balle.io/) as a Student Researcher.

[![Google Scholar](https://img.shields.io/badge/Google%20Scholar-4285F4?style=for-the-badge&logo=google-scholar&logoColor=white)
](https://scholar.google.com/citations?user=5bQjLz4AAAAJ&hl=en)
[![X (Twitter)](https://img.shields.io/badge/X-000000.svg?style=for-the-badge&logo=X&logoColor=white)
](https://twitter.com/_dsevero)
[![CV](https://img.shields.io/badge/CV%20&#40;last%20updated%20October%202023&#41;-009900?style=for-the-badge&logoColor=white)](https://dsevero.com/cv.pdf)


# Research Interests
I'm interested in information theory, machine learning, and AI.

### Compression of non-sequential data
Lossless compression algorithms typically preserve the ordering in which data points are compressed.
However, there are data types where order is not meaningful, such as collections of files, rows in a database, nodes in a graph, and, notably, datasets in machine learning applications.

Compressing with traditional algorithms is possible if we pick an order for the elements and communicate the corresponding ordered sequence.
However, unless the order information is somehow removed during the encoding process, this procedure will be sub-optimal, because the order contains information and therefore more bits are used to represent the source than are truly necessary.

In previous works, we gave a formal definition for non-sequential objects as random sets of equivalent sequences, which we call _Combinatorial Random Variables_ (CRVs), as well as a general class of computatioanlly efficient algorithms that achieve the optimal compression rate of CRVs: _Random Permutation Codes_ (RPCs).
Specialized RPCs are given for the case of multisets ([Random Order Coding](https://arxiv.org/abs/2107.09202)), graphs ([Random Edge Coding](https://arxiv.org/abs/2305.09705)), and partitions/clusterings (under review), providing new algorithms for compression of databases, social networks, and web data in the JSON file format.

# Latest News
**April 2024** - I've moved to Montréal to start as a Research Engineer at FAIR Labs!

**March 2024** - [The Unreasonable Effectiveness of Linear Prediction as a Perceptual Metri](https://arxiv.org/abs/2310.05986) and [Entropy Coding of Unordered Data Structures](https://openreview.net/pdf?id=PggJ9CbEN7) were accepted to ICLR 2024.

**August 2023** - I started a second internship at FAIR (Meta AI) in information theory and generative modelling with [Matthew Muckley](https://mmuckley.github.io/).

**April 2023** - [Random Edge Coding](https://arxiv.org/abs/2305.09705) and [Action Matching](https://arxiv.org/abs/2210.06662) were accepted to ICML 2023.

# Tutorials and Workshops
- [ICML 2023 Workshop on Neural Compression and Information Theory](https://neuralcompression.github.io/workshop23), 2023
- [Asymmetric Numeral Systems (ANS) codec in pure Python](https://gist.github.com/dsevero/7e02d96e079ce44b89ff33d7a1ce1738), 2021
- [A tutorial on bits-back with Huffman coding](https://gist.github.com/dsevero/8e7c38b44953964d3b9873b6bd96d9b2), 2021
- [Vectorized Run-Length Encoding](https://gist.github.com/dsevero/693677754798e21f539e4e11a3103576), 2021
- [Persisting lru_cache to disk while using hashable pandas objects for parallel experiments](https://gist.github.com/dsevero/252a5f280600c6b1118ed42826d188a9), 2020

# Recommended readings (not my authorship)
- [Darts, Dice, and Coins: Sampling from a Discrete Distribution](https://www.keithschwarz.com/darts-dice-coins/) by Keith Schwarz, 2011


# Selected Publications and Preprints
For a complete list, please see my [Google Scholar](https://scholar.google.com/citations?user=5bQjLz4AAAAJ&hl=en) profile.

<div align="center">
<table>
  <tr>
    <td width="30%"><img src="static/lasi-thumbnail.png" width="300"></td>
    <td width="70%">
      <b>The Unreasonable Effectiveness of Linear Prediction as a Perceptual Metric</b><br>
      <u>Daniel Severo</u>, Lucas Theis, Johannes Ballé<br>
      International Conference on Learning Representations (ICLR), 2024<br>
      <a href="https://arxiv.org/abs/2310.05986"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
      <a href="https://github.com/dsevero/Linear-Autoregressive-Similarity-Index"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    </td>
  </tr>
  <tr>
    <td width="30%"><img src="static/rec.svg" width="300"></td>
    <td width="70%">
      <br>
      <b>Random Edge Coding: One-Shot Bits-Back Coding of Large Labeled Graphs</b><br>
      <u>Daniel Severo</u>, James Townsend, Ashish Khisti, Alireza Makhzani<br>
      International Conference on Machine Learning (ICML), 2023 <br>
      <a href="https://arxiv.org/abs/2305.09705"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
      <a href="https://github.com/dsevero/Random-Edge-Coding"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
    </td>
  </tr>
  <tr>
    <td width="30%"><img src="static/am-thumbnail.png" width="300"></td>
    <td width="70%">
      <br>
      <b>Action Matching: Learning Stochastic Dynamics from Samples</b><br>
      Kirill Neklyudov, Rob Brekelmans, <u>Daniel Severo</u>, Alireza Makhzani<br>
      International Conference on Machine Learning (ICML), 2023 <br>
      <a href="https://arxiv.org/abs/2210.06662"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
      <a href="https://github.com/necludov/jam"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
      <a href="https://www.youtube.com/watch?v=35uEI5ryDRQ"><img src="https://img.shields.io/badge/video-0A75AD.svg?logo=youtube&style=flat"></a>
    </td>
  </tr>
  <tr>
    <td width="30%"><img src="static/bbms-thumbnail-pop.png" width="200"></td>
    <td width="70%">
      <b>Compressing Multisets with Large Alphabets using Bits-Back Coding</b><br>
      <u>Daniel Severo</u>, James Townsend, Ashish Khisti, Alireza Makhzani, Karen Ullrich<br>
      IEEE Journal on Selected Areas in Information Theory, 2023<br>
      <span style="color:red"><b>Best Paper Award</b></span> at NeurIPS Workshop on DGMs, 2021<br>
      <a href="https://arxiv.org/abs/2107.09202"><img src="https://img.shields.io/badge/arXiv-b31b1b.svg?style=flat"></a>
      <a href="https://github.com/facebookresearch/multiset-compression"><img src="https://img.shields.io/badge/code-grey.svg?logo=github&style=flat"></a>
      <a href="https://youtube.com/watch?v=Gwf9_t-JjsQ"><img src="https://img.shields.io/badge/video-0A75AD.svg?logo=youtube&style=flat"></a>
      <a href="https://dsevero.com/severo-townsend-dcc22-multisets.pdf"><img src="https://img.shields.io/badge/slides-065535.svg?logo=latex&style=flat"></a>
    </td>
  </tr>
</table>
</div>
