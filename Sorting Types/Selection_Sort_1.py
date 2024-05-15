Tuple = [4,5,1,3,6,9,2]
print(Tuple)
for u in range(0,len(Tuple)): # Note len(Tuple) not include

	for v in range(u+1,len(Tuple)): # Note len(Tuple) not include
		
		if Tuple[u] > Tuple[v]:

			Temp = Tuple[v]

			Tuple[v] = Tuple[u]

			Tuple[u] = Temp

print(Tuple)