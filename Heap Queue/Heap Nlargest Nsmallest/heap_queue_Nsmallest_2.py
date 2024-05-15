from heapq import nsmallest

# help(nsmallest)

Tuple = ('a','b','d','f','c','a','b')
print(Tuple)
Number = nsmallest(n=2,iterable=Tuple)
print()
print(f'Largest Number in the Tuple:{Number}')