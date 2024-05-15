from pandas import Series
# this method is used for to replace the false value
# Replace values where the condition is False.

# help(Series.where)

S=Series(range(5))
print(S)

print(S.where(S>2))
print()
# see the help for other and for parameter
print(S.where(S<3,other=99))