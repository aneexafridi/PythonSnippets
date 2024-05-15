from heapq import nlargest

# help(nlargest)

Tuple = ('a','f','e','c','d','b','f','c')
print(Tuple)
Number = nlargest(n=2,iterable=Tuple)
print()
print(f'Largest Number in the Tuple:{Number}')