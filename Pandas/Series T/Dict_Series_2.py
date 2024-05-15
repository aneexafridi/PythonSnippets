from pandas import Series

Dict = {'a':0.,'b':1.,'c':2.}
print(Dict,'\n')
# Dictionary keys are used to construct index
print(Series(data=Dict))