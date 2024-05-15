from pandas import Series
# help(Series.update)

S1 = Series(data=('a','b','d'),index=(1,2,3))
print(S1)
S2 = Series(data=('c'), index=(3,))
S1.update(S2)
print(S1)

# s = Series(['a', 'b', 'c'])
# s.update(Series(['d', 'e'], index=[0, 2]))
# print(s)