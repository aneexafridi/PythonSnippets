# help(map)

List = [1,2,3]
print(List)

for u in  range(len(List)):
	List[u] *=2
print(List)

# Equivalent below code
print()
List =list(map((lambda x:x*2),[1,2,3]))
print(List)