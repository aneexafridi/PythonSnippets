# List = [1,2,3,4,[55,66,77,88]]
# for u in range(len(List)):
# # check each element of list where element or list
# 	if(type(List[u]) is list): 
# 		for v in range(len(List[u])):
# 			print(List[u][v],end=' ')
# 	else:
# 		print(List[u],end=' ')

# # without index for Loop

List = [[1,2,3,4],[55,66,77,88]]
for u in List:
	for v in u:
		print(v,end=' ')
	print()