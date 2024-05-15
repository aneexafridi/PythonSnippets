# we are add new column to existing data frame

from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(4,5,6),index=('a','b','c')),
		'three':Series(data=(11,12,13,14),index=('a','b','c','d'))
		}
DF = DataFrame(data=Dict)
print(DF)

# Adding a new column to an existing data frame
print("\nAfter Delete the Column Three")
print("using del Function\n") 

# del DF['three']
# more efficient
DF.drop(columns='three',inplace=True)

print(DF)