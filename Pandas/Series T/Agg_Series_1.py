from pandas import Series
#  'agg' is aggregate
#  help(Series.agg)

Dict = {'a':1,'b':2,'c':3}
List = [1,2,3]
print(Dict)
print(List)

print(Series(data=Dict))
print(Series(data=Dict).agg('min'))
print(Series(data=Dict).agg('max'))
print("Combine both max and min:\n")
print(Series(data=Dict).agg(['min','max']))

