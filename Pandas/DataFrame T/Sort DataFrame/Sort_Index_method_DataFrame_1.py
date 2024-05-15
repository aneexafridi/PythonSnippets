from pandas import DataFrame
# help(DataFrame.sort_index)

#(axis=0, level=None, ascending=True, inplace=False, kind='quicksort',
# na_position='last', sort_remaining=True, ignore_index=False, key=None)

DF = DataFrame(data=list('ABCD'),columns=('First',),index=(4,1,3,2))
print(DF)
print('\n\n')
print(DF.sort_index())
