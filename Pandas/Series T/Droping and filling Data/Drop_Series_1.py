from pandas import Series
from numpy import nan
# help(Series.dropna) # for more information

S = Series(data=['Ali',nan,'Shahab'],index=list('abc'))
print(S)

print('\n')
print('After the dropna method use')
print(S.dropna())
# can passing the replace = True
