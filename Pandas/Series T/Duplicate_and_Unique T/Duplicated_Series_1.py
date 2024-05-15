from pandas import Series
# help(Series.duplicated)

S = Series(data=('cat','dog','cow','cat','dog'))
print(S)
print("\nduplicated method used")
print(S.duplicated())

# this method
# return the boolean values series