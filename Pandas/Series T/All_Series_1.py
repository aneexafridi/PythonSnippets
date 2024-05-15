from pandas import Series

print(Series(data=[True,False]).all())
print()
print(Series(data=[True,True]).all())
print()
print(Series(data=[]).all())