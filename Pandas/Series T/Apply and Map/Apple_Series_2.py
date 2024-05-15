from pandas import Series
# help(Series.apply) # for more information

S = Series(data=[1,2,3,4],index=list('ABCD'))
print(S)
print()
print('After the Series apply method for Muliple')
print(S.apply(lambda x:x*3))