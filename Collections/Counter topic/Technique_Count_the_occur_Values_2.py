# List = ['c','a','b','c','d','a','b','a','d','e']
# same above comment List
List = list('cabcdabade')
print('List\n',List)

Set = set(List)
print('Set\n',Set)
#using set for to remove the duplicate values from list
Dict = dict() # empty dict

for u in sorted(Set):
	Dict[u] = List.count(u)
# Dict[u]  creating key then storing the value
# Note List.count() checking for each value in the List
print('Dict\n',Dict)
# convertion for convenient view
# tuple(Dict),set(Dict),list(Dict)