from pandas import Series

# help(Series.groupby)

S = Series(data=(2,4,6,10),index=('1','2','3','4'))
print(S)

print()
print(S.groupby(by=['a','a','b','b']).mean()) # sum()
# (a+b)/2 = value again next (b+b)/2 =value
print()
print(S.groupby(by=['a','b','a','b']).mean()) # sum()
# (a +b) / 2 = value again next (a+b)/ 2 =value

print()
print(S.groupby(by=['a','b','c','d']).mean()) # sum()
# here just assigned the values becuase  these are no 
# any group between them
