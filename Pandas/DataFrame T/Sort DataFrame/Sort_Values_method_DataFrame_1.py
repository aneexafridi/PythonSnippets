from pandas import DataFrame

# help(DataFrame.sort_values)

# DataFrame.sort_values(by, axis=0, ascending=True, inplace=False,
# kind='quicksort', na_position='last', ignore_index=False, key=None)
Dict  = {
		"First":['D','A','C','B'],
		"Second":['G','F','H','E']
		}

DF = DataFrame(data=Dict)
print(DF)
print('\n')
# print(DF.sort_values(by=['First','Second'],ascending=[True,False]))
print(DF.sort_values(by='First'))