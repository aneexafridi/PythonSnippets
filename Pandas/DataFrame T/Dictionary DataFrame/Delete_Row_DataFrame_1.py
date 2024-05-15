from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(4,5,6),index=('a','b','c')),
		'three':Series(data=(11,12,13,14),index=('a','b','c','d'))
		}
DF = DataFrame(data=Dict)
print(DF)

# Adding a new Row to an existing data frame
print("\nAfter Delete the Row b")
print("using del Function\n") 

DF.drop(index='b',inplace=True)

print(DF)