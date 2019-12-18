---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Learning From Data, Problem 1.7"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2019-12-12T19:37:27-03:00
lastmod: 2019-12-12T19:37:27-03:00
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

> A sample of heads and tails is created by tossing a coin a number of times independently. Assume we have a number of coins that generate different samples independently. For a given coin, let the probability of heads (probability of error) be $\mu$. The probability of obtaining $k$ heads in $N$ tosses of this coin is given by the binomial distribution:
> $$ P\\left[ k \\mid N, \\mu \\right] = {N\\choose k} \\mu^k \\left(1 - \\mu\\right)^{N-k}$$
> Remember that the training error $\\nu$ is $\frac{k}{N}$

The objective of this problem is to show that, given a large enough set of hypotheses $\\mathcal{H}$, the probability of obtaining low training error on at least one $h \\in \\mathcal{H}$ is high if the data is i.i.d. Therefore, we should be careful when evaluating models even if we have followed the standard train, test and validation split procedure.

How does this translate to practice? Say you have a training dataset $\\mathcal{D}$ and $M$ models $h\_m \\in \\mathcal{H}$ that you wish to evaluate. You sample (with replacement) $N$ points $\\mathbf{x}\_{m,n} \\in \\mathcal{D}$ (e.g. mini-batch training) for each $h\_m$ (i.e. a total of $NM$ points). What is the probability that at least one hypothesis will have low in-sample error?

A coin flip represents a data point $\\mathbf{x} \\in \\mathcal{X}$, therefore $N$ is the size of the dataset. Each coin is a hypothesis $h \\in \\mathcal{H}$, hence $M$ is the cardinality of $\mathcal{H}$. Following the bin analogy from the book, heads (numerically, $1$) represents a _miss_ $h(\mathbf{x}) \neq f(\mathbf{x})$ where $f: \\mathcal{X} \\rightarrow \\left\\{\\text{heads}, \\text{tails}\\right\\}$ is the target function.

> (a) Assume the sample size $(N)$ is $10$. If all the coins have $\\mu = 0.05$ compute the probability that at least one coin will have $v = 0$ for the case of $1$ coin, $1,000$ coins, $1,000,000$ coins. Repeat for μ = 0.8.

Let $k\_m$ be the number of heads for each coin. Since $\\nu=0$ implies that $k=0$, we need to calculate

$$ P\\left[ k\_1=0 \vee k\_2=0 \vee ... k\_m=0 \\right] = P\\left[ \\bigvee\\limits\_{m} k\_m = 0 \\right]$$

Here, we employ the common trick of computing the probability of the complement

$$
\begin{aligned}
  P\\left[ \\bigvee\\limits\_{m} k\_m = 0 \\right] &= 1 - P\\left[ \\bigwedge\\limits\_{m} k\_m > 0 \\right] \\\\\\
                                                   &= 1 - \\prod\\limits\_{m}P\\left[ k\_m > 0 \\right]
\end{aligned}
$$

Note that this step follows from the fact that $\\mathbf{x}\_{m,n}$ are independent. If we had used the same set of $N$ points for all $h\_m$ (i.e. $\\mathbf{x}\_{m,n} \\rightarrow \\mathbf{x}\_{n})$, the set of $k\_m$ would not be independent, since looking at a specific $k\_m$ would give you information regarding some other $k\_{m^\\prime}$.

Summing over the values of $k$ and using the fact that $\\sum\\limits_{k=0}^N P\\left[k\\right] = 1$ we can compute 

$$
\begin{aligned}
  P\\left[ k\_m > 0 \\right] &= \\sum\\limits\_{i=1}^N P\\left[k\\right] \\\\\\
                             &= \\sum\\limits\_{i=0}^N P\\left[k\\right] - P\\left[0\\right] \\\\\\
                             &= 1 - \\left(1 - \\mu\\right)^N
\end{aligned}
$$

Thus, resulting in

$$P\\left[ \\bigvee\\limits\_{m} k\_m = 0 \\right] = 1 - \\left(  1 - \\left(1 - \\mu\\right)^N \\right)^M$$

The result is intuitive. For a single coin, if $\\left(1 - \\mu\\right)^N$ is the probability that **all** $N$ flips result in tails, the complement $1 - \\left(1 - \\mu\\right)^N$ is the probability that **at least one** flip will result in heads. For this to happen to **all** $M$ coins, we get $\\left(  1 - \\left(1 - \\mu\\right)^N \\right)^M$. Similarly, the probability of the complement is $1 - \\left(  1 - \\left(1 - \\mu\\right)^N \\right)^M$ and can be interpretated as the probability that **at least one** coin out of $M$ will have **at least one** flip out of $N$ resulting in heads.

Let's take a look at this in python.

```python
import matplotlib.pyplot as plt
import pandas as pd

def prob_zero_error(μ: 'true probability of error',
                    M: 'number of hypotheses',
                    N: 'number of data points'):
    return 1 - (1 - (1 - μ)**N)**M

d = [{'μ': μ, 
      'M': M, 
      'p': prob_zero_error(μ, M, N=10)} 
     for μ in [0.05, 0.8] 
     for M in [1, 1_000, 1_000_000]]

pd.DataFrame(d).pivot('M', 'μ', 'p').to_html()
```

<table>
  <thead>
    <tr style="text-align: right;">
      <th>μ</th>
      <th>0.05</th>
      <th>0.8</th>
    </tr>
    <tr>
      <th>M</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.598737</td>
      <td>1.024000e-07</td>
    </tr>
    <tr>
      <th>1000</th>
      <td>1.000000</td>
      <td>1.023948e-04</td>
    </tr>
    <tr>
      <th>1000000</th>
      <td>1.000000</td>
      <td>9.733159e-02</td>
    </tr>
  </tbody>
</table>

> (b) For the case $N = 6$ and $2$ coins with $\\mu = 0.5$ for both coins, plot the probability $$P\[ \\max\\limits\_i \\mid \\nu\_i - \\mu\_i \\mid > \\epsilon \]$$ for $\\epsilon$ in the range $\[0, 1\]$ (the max is over coins). On the same plot show the bound that would be obtained using the Hoeffding Inequality. Remember that for a single coin, the Hoeffding bound is $$P\[\\mid \\nu- \\mu \\mid > \\epsilon \] \\leq 2e^{-2N\\epsilon^2}$$

<!---
> [Hint: Use $P\[A\\space\\text{or}\\space B\] = P\[A\] + P\[B\] \\space \\space \\space \\space P\[A\\space\\text{and}\\space B\] = P\[A\] + P\[B\] - P\[A\] P\[B\]$, where the last equality follows by independence, to evaluate $P\[\\max \\dots \]]$.
-->

---
