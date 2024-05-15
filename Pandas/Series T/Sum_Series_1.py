from pandas import Series

# help(Series.sum)

S = Series(data=[1,2,3,4])
print(S)
print("Series.sum : ",S.sum())
# built-in function used both same resulted
print("built-in sum : ",sum(S))