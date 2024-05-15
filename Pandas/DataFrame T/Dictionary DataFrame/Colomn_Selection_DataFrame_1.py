from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(11,12,13,14),index=('a','b','c','d'))
		}
# we do not pass label d and assigned NaN
DF = DataFrame(data=Dict)
print(DF)

print("\n\n")
print("Column one\n")
print(DF['one']) #pass here key of the dictionary
