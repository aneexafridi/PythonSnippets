# from collections import Counter
# C = Counter(('a','b','c','d','a','b','a'))
# print(C)

List = ['a','b','c','d','a','c']
print(List)
Set = set(List)
print(Set)
Count = dict() # empty dict
for u in Set:
	Count[u] = (List.count(u))
print(Count)