# we are add new column to existing data frame and
# concatenating the two columns

from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(11,12,13,14),index=('a','b','c','d'))
		}
DF = DataFrame(data=Dict)
print(DF)

# Adding a new column to an existing data frame
print("\nAfter the Adding  column Three to DataFrame\n")

DF['three'] = Series(data=(4,5,6),index=('a','b','c'))
print(DF)
print()

print("\nAfter the Adding two columns to DataFrame\n")
DF['four'] = DF['one'] + DF['two']
print(DF)