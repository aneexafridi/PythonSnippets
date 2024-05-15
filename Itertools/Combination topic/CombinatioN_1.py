# combinations(iterable, r)
#  |  
#  |Return successive r-length combinations of elements in the iterable.
#  |  
#  |combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)

from itertools import combinations

# help(combinations)

Cob = combinations(iterable=[1,2,3],r=2)
print(list(Cob))

Cob = combinations('abc',r=2)
print(list(Cob))
