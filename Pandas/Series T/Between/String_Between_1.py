from pandas import Series
List = ['a','b','c','d','e','f','g','h']
S = Series(data=List)
# Return boolean Series equivalent to left <= series <= right.
print(S.between('c','f'))