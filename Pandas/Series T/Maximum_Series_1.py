from pandas import Series

# help(Series.max)

S = Series(data=[1,2,3,4])
print(S)
print("Series.Maximum : ",S.max())
# built-in function used both same resulted
print("built-in max : ",max(S))