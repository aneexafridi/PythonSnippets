from pandas import Series
# help(Series.duplicated)

S = Series(data=('cat','dog','cow','cat','dog'))
print(S)

print(S.duplicated())

# return the Series of boolean values