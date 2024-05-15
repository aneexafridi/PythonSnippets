from heapq import nlargest

# help(nlargest)

Tuple = (1,2,3,4,5,6,7,8,9,10)
print(Tuple)
Number = nlargest(n=1,iterable=Tuple)
print()
print(f'Largest Number in the Tuple:{Number}')