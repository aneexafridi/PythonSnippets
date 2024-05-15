from pandas import Series
from numpy import array,arange
Array = array(['A','B','C','D'])
print(Array,"\n")
print(Series(data=Array))
print()
print(Series(data=Array,index=[101,102,103,104]))