# we are add new column to exist data frame

from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(11,12,13,14),index=('a','b','c','d'))
		}
DF = DataFrame(data=Dict)
print(DF)

# Adding a new column to an exist data frame
print("\nAfter the Adding the new column to DataFrame\n")

DF['three'] = Series(data=(4,5,6),index=('a','b','d'))

print(DF)