---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "Learning From Data, Exercise 1.10"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2019-12-11T22:14:05-03:00
lastmod: 2019-12-11T22:14:05-03:00
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

# Statement

Here is an experiment that illustrates the difference between a single bin and multiple bins. Run a computer simulation for flipping 1,000 fair coins. Flip each coin independently 10 times. Let's focus on 3 coins as follows: $c\_1$ is the first coin flipped; $c\_{rand}$ is a coin you choose at random; $c\_{min}$ is the coin that had the minimum frequency of heads (pick the earlier one in case of a tie). $\\nu\_1$, $\\nu\_{rand}$ and $\\nu\_{min}$ be the fraction of heads you obtain for the respective three coins.

**(a) What is $\\mu$ for the three coins selected?**

(b) Repeat this entire experiment a large number of times (e.g., 100,000 runs of the entire experiment) to get several instances of $\\nu\_1$, $\\nu\_{rand}$ and $\\nu\_{min}$ and plot the histograms of the distributions of $\\nu\_1$, $\\nu\_{rand}$ and $\\nu\_{min}$. Notice that which coins end up being $c\_{rand}$ and $c\_{min}$ may differ from one run to another.

\(c\) Using (b), plot estimates for $\\mathbb{P}\\left[\\lvert \\nu - \\mu \\rvert > \\epsilon\\right]$ as a function of $\\epsilon$, together with the Hoeffding bound $2e^{-2\\epsilon^2N}$ (on the same graph).

(d) Which coins obey the Hoeffding bound, and which ones do not? Explain why.

(e) Relate part (d) to the multiple bins in Figure 1.10.
