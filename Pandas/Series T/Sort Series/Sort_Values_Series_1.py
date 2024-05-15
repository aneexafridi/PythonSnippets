from pandas import Series

# help(Series.sort_values)

# using list method each single character seperate by coma
print(list('bd9a1c'))

S = Series(data=list('bd9a1c'))
print("See with no parameter")
print(S.sort_values(),'\nSee with ignore_index= True')
print(S.sort_values(ignore_index=True))
# by default set True now expl
print("\nSee the ascending")
print(S.sort_values(ascending=False)) 