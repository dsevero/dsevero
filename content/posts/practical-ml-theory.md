---
title: "Practical Machine Learning Theory"
draft: true
---

```python3
𝓗 = [lambda x: x > 0.25,
     lambda x: x > 0.50,
     lambda x: x > 0.75]

P = [(0.1, (0.0, 0)),
     (0.1, (0.1, 0)),
     (0.1, (0.2, 0)),
     (0.1, (0.3, 0)),
     (0.1, (0.4, 0)),
     (0.1, (0.5, 1)),
     (0.1, (0.6, 1)),
     (0.1, (0.7, 1)),
     (0.1, (0.8, 1)),
     (0.1, (0.9, 1))]

def L(h, P):
  return sum(p*ℓ(h, z) for p, z in P)

def ℓ(h, z):
  return int(h(z[0]) != z[1])

def 𝓐(S):
  h, loss = sorted([(h, L(h, S)) for h in 𝓗], 
                   key=lambda t: [0])[0]
  return h
```
