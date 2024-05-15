from pandas import Series

# help(Series.append)
# series (data = iterable type) list tuple string
S1 = Series(data=(1,2,3))
S2 = Series(data=[4,5,6])
print(S1)
print(S2)
print("After the mehtod append with out ignore Index")
print(S1.append(S2))
print()
print("After the mehtod append with ignore Index")
print(S1.append(S2,ignore_index= True))
