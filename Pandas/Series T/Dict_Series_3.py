from pandas import Series
from numpy import array,arange
Dict = {'a':1,'b':2,'c':3}
print(Dict,'\n')
# --------------------Note------------------
# Dictionary keys are used to construct index
print(Series(data=Dict,index=['a','b','c','d']))