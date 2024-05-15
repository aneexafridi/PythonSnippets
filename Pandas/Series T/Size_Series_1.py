from pandas import Series

# help(Series.size)

print(Series(data=[1,2,3,4]).size)


Dict = {'a':1,'b':2,'c':3}
print(Series(data=Dict).size)

print() # size count the index 
Dict = {'a':1,'b':2,'c':3}
print(Series(data=Dict,index=['a','b','c','d']).size)