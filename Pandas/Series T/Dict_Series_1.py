from pandas import Series

Dict = {'a':1,'b':2,'c':3,'d':4}
print(Dict)

print(Series(data=Dict))
print('\n\n')

S = Series(data={1:'a',2:'b',3:'c',4:'d'})
print(S)

print(S.apply(lambda x:x.upper()))