# If a label is not contained, an exception is raised.

from pandas import Series

S1 = Series(data=[1,2,3,4,5],index=['a','b','c','d','e'])
print(S1)
print() # line 6 and line 8 are same output
print(S1[['a','b','c','d','e']])

# retrieve a single element
print(S1['a'])
print(S1['d'])
print()

# here see exception 
print(S1['u'])