from pandas import DataFrame,Series

Dict = {
		'one':Series(data=(1,2,3),index=('a','b','c')),
		'two':Series(data=(1,2,3,4),index=('a','b','c','d'))
		}
# we do not pass for label d and appended NaN

print(DataFrame(data=Dict))