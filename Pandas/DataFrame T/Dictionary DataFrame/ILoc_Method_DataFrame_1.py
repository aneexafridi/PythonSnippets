from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(4,5,6),index=('a','b','c')),
		'three':Series(data=(11,12,13,14),index=('a','b','c','d'))
		}
DF = DataFrame(data=Dict)
print(DF)

print("\nUsing the iloc Function for select Row")
print(DF.iloc[2])

# using index for row
# iloc method parameter passing the index (int)
# remember difference between loc and iloc