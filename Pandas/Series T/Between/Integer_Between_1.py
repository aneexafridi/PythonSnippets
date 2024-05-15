from pandas import Series
List = [1,2,3,4,5,6,7,8,9]
S = Series(data=List)
# Return boolean Series equivalent to left <= series <= right.
print(S.between(3,7))