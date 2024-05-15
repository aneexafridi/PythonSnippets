from operator import itemgetter

List = [('Apple',2),('Orange',1),('Banana',5),('pear',3)]
print(List)
print()

def Sorted_by_itemgetter():
	print(sorted(List,key=itemgetter(1)))

def Sorted_by_lambda():
	print(sorted(List,key=lambda x:x[1]))

print('Sorting by the lambda key')
Sorted_by_itemgetter()
print('\n')
print('Sorting by the itemgetter key')
Sorted_by_lambda()

#----------------------Note return the each index
# sorted(List,key=itemgetter(1))
# sorted(List,key=lambda x:x[1])

# in List each element here (each element mean) Tuple like ('apple',1)
# key function will performing mean "('apple',1)[1]"   which is second index of Tuple









