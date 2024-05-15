from pandas import Series

S = Series(data=['a',1,3.14])
print(S)
print('Dype of Series: ',S.dtype)
print('\n')

S = Series(data=[1,2.2])
print(S)
print('dtype of Series: ',S.dtype)
S = Series(data=(1,2,3))
print(S)
print('dtype of Series: ',S.dtype)