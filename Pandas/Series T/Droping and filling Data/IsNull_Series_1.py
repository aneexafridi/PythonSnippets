from pandas import Series
from numpy import nan
# help(Series.isnull) # for more information

S = Series(data=(1,nan,'',4,'Z'),index=list('abcde'))
print(S)

print('\n')
print('After the isnull method use')
print(S.isnull())

