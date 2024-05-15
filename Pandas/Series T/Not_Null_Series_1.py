from pandas import Series
# help(Series.notnull)

Dict = {'a':1,'b':2,'c':3}
print(Series(data=Dict,index=['a','b','c','d']))
print()

print(Series(data=Dict,index=['a','b','c','d']).notnull())