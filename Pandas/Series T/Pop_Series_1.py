from pandas import Series
# Return item and drops from series. Raise KeyError if not found.

# help(Series.pop)
List = list('abcd')
print(List)
print()

# passing the index of the element

# return the pop up value
S = Series(data=List)
print(S)
print(S.pop(1))
print("After pop up  from the List")
print(S)
