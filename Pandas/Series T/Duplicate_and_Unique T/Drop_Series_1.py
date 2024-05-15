from pandas import Series

# help(Series.drop)
# Return Series with specified index labels removed.

S = Series(data=(1,2,3,4),index=('a','b','c','d'))
print(S)
print(S.drop(labels='c'))
# we can use index instead of labels
S = Series(data=list('ABCD'))
print(S)
print(S.drop(index=2))