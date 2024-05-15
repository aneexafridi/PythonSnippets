from pandas import Series

# help(Series.unique)
S = Series(data=('a','b','a','c','b'),name = "S Series")
print(S)

# unique value
print("\nAfter checking the unique values in Series")
# The unique values returned as a NumPy array
print(S.unique())