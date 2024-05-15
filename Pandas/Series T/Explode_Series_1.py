from pandas import Series
from numpy import nan
# help(Series.explode) # for more information

S = Series(data=('Ali',nan,['Shahab',4],[0],('a',3)))
print(S)

print('\n')
print('After the Explode method use')
print(S.explode(ignore_index=True))

