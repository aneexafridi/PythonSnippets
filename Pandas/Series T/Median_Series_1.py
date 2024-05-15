from pandas import Series
# help(Series.median)

S = Series(data=(1,2,3,4,5),index=('a','b','c','d','e'))
print(S)
print("median method")
print(S.median())