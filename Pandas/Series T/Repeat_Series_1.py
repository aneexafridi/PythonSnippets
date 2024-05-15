from pandas import Series
# help(Series.repeat)

S = Series(data=(1,2,3),index=('a','b','c'))
print(S)
print()
print(S.repeat(2))
print()
print(S.repeat([1,2,3]))