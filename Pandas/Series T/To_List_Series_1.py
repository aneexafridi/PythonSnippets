from pandas import Series

# help(Series.to_list) # for information

print(Series(data=(1,2,3,4)))
print()
print(Series(data=(1,3,3,4)).to_list())