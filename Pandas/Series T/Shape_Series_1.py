from pandas import Series

print(Series(data=[1,2,3]).shape)


Dict = {'a':1,'b':2,'c':3}
print(Series(Dict).shape)

print()
Dict = {'a':1,'b':2,'c':3}
print(Series(Dict,index=['a','b','c','d']).shape)