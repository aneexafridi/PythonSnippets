from pandas import Series
# help(Series.mean)

S = Series(data=(1,2,3,4),index=('a','b','c','d'))
print(S)
print("mean method")
print(S.mean())