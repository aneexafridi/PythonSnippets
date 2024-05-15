List = [5,2,1,9,4]
print(List)
print('\nAfter sorting')
for u in range(len(List)):
	for v in range(u,len(List)):
		if List[u]>List[v]:
			List[u],List[v] = List[v],List[u]


print(List)