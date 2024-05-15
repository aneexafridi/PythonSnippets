from itertools import permutations

# permutations(iterable, r=None)
# help(permutations)

 # formula  p = n!/(n-r)!

A = [1,2]
print(A)
print()
Result = permutations(A)
print(list(Result))
print()
Result = permutations([1,2,3],r=2)
print(list(Result))