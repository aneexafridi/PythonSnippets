from pandas import Series
# help(Series.product) # for more information

#________________Note________________________
# see prod built-in function in math module

S = Series(data=(3,2,6),index=list('abc'))
print(S)

print('\n')
print('After the Prod method use')
print(S.product())

# prod method and product method is same