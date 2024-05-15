from itertools import permutations
# permutations(iterable, r=None)
# help(permutations)

def Permutation(iterable,r=None):
	Per=permutations(iterable,r=None)
	print(list(Per))

Permutation([1,2],2)