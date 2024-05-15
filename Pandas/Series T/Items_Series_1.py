from pandas import Series
#This method returns an iterable tuple (index, value).
#This is convenient if you want to create a lazy iterator.

# help(Series.item)

# for list 
List = ['a','b','c']
print(List,'\n')

print('\nSeries dictionary')
for n,v in Series(List).items():
	print(f'{n} = {v}')

# for Dictionary
Dict = {"a":1,"b":2,"c":3}
print(Dict,end='')
print('\nSeries dictionary')
for k,v in Series(data=Dict).items():
	print(f'{k} = {v}')