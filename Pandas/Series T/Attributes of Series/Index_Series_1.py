from pandas import Series
S = Series(data=(1,2,3),index=list('abc'))
print(S)
print("index of Series: ",S.index)

print('\n')

S = Series(data=(1,2,3))
print(S)
print("index of Series: ",S.index)