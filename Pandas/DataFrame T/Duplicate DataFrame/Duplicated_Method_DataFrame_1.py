from pandas import DataFrame
# help(DataFrame.duplicated)
Dict = {
		"Animals":('Cow','Goat','Dog','Cat','Dog')
		}

DF = DataFrame(data=Dict)
# By default, for each set of duplicated values, the first 
# occurrence is set on False and all others on True.
print(DF)
print()
print(DF.duplicated())



