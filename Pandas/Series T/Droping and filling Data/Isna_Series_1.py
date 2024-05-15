from pandas import Series
from numpy import nan
# help(Series.isna) # for more information

S = Series(data=(nan,2,nan,4),index=list('abcd'))
print(S)

print('\n')
print('After the isna method use')
print(S.isna())

# for nan return True and for others False

