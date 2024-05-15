from math import comb

# help(comb) must check out

# Syntax:      comb(n,k,/)
# Evaluates to n! / (k! * (n - k)!)
 # when k <= n and evaluates to zero when k > n.

Combination = comb(7,3)
print(Combination)

# and also check  the itertools library Combination topic