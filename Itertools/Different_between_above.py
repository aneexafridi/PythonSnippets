# Examples                  =         Results
 # formula  (a-b)^n not exact this for some cases
# product('ABCD', repeat=2) = AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
 # formula  p = n!/(n-r)!
# permutations('ABCD', 2)   = AB AC AD BA BC BD CA CB CD DA DB DC
# formula   C = n!/(n-r)!r!
# combinations('ABCD', 2)   = AB AC AD BC BD CD

# combinations_with_replacement('ABCD', 2) = AA AB AC AD BB BC BD CC CD DD

from itertools import product,permutations,combinations

print(list(product('ABC',repeat=2)))
print()
print(list(permutations('ABC',2)))
print()
print(list(combinations('ABC',2)))