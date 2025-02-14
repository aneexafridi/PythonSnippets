	# tertools.compress(data, selectors)
# Make an iterator that filters elements from data returning only those that have a corresponding element in selectors that evaluates to True. Stops when either the data or selectors iterables
# has been exhausted.Roughly equivalent to:

# def compress(data, selectors):
#     compress('ABCDEF', [1,0,1,0,1,1]) #--> A C E F
#     return (d for d, s in zip(data, selectors) if s)

from itertools import compress
# help(compress)

Colors = [11,22,33,44,55,66,77]
Select = [True,False,True,False,True,True,False] 
# Note selectors are must be iterable of bool type or
# digits (0,or 1) else number not work 0 for False, 1 for True
print(Colors)

Comp = compress(data=Colors,selectors=Select)
print(list(Comp))