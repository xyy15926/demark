#!/usr/bin/env python3
#----------------------------------------------------------
#   Name: spy.py
#   Author: xyy15926
#   Created at: 2020-11-17 08:53:36
#   Updated at: 2020-11-17 08:54:02
#   Description: Notes for studying scipy, including some
#     code
#----------------------------------------------------------

# %%
import scipy
from scipy import special

# %% [markdown]
# Special Functions
#
# |Function|Expression|
# |-----|-----|
# |`special.exp10(x)`|$10^x$|
# |`special.zeta(x, q)`|$\sum_{n=0}^{\infty} \frac 1 {(n+q)^x}$|
# |`special.zetac(x)`|$\sum_{n=2}^{\infty} \frac 1 {n^x}$|

print(scipy.special.exp10(-1))
print(scipy.special.zeta(2, 1))
print(scipy.special.zetac(2))

# %%
