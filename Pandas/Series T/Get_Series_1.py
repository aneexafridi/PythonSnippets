from pandas import Series
# help(Series.get)
# # syntax: 
# 		Series.get(key,default=None)
# 		key = object -> mean object can be list or scalar value,str,int

S = Series(data=(1,2,3),index=list('abc'))
print(S)
print()
# return the value of the Series
print(S.get('b'))
print(type(S.get('b')))
print()
print(S.get(['a','c']))
print(type(S.get(['a','c'])))