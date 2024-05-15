from pandas import Series
from numpy import nan
# help(Series.fillna) # for more information

S = Series(data=['Ali',nan,'Shahab'],index=list('abc'))
print(S)

print('\n')
print('After the fillna method use')
print(S.fillna(value=99))

