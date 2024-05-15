from pandas import Series

S = Series(data=['a','b','c'])
print(S)

print(S.name)


S.name = 'My_Series'

print(S.name)