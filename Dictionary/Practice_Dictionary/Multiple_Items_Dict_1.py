Dict = {1:10,2:20,3:30}
print(Dict)
i=1
for keys,values in Dict.items():
	# print(keys,values)
	Dict[i] = values *9
	i+=1
print(Dict)
	