from pandas import Series

# help(Series.min)

S = Series(data=[1,2,3,4])
print(S)
print("Series.min : ",S.min())
# built-in function used both same resulted
print("built-in min : ",min(S))