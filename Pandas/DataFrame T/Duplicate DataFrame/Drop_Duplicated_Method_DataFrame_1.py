from pandas import DataFrame
# help(DataFrame)
# DataFrame.drop_duplicates(subset=None, keep='first',
# inplace=False, ignore_index=False)

Dict = {
		"Animals":('Cow','Dog','Goat','Dog')
		}
DF = DataFrame(data=Dict)
print(DF)
print('\n')
print(DF.drop_duplicates(keep='last'))
# print(DF.drop_duplicates(keep='first'))
