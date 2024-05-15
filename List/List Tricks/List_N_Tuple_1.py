# created by the firsts elements in the tuple
List = [(1,2),(3,4),(5,6),(7,8),(9,10)]
# List = [[1,2],[3,4],[5,6],[7,8],[9,1]]

print()
print(list(zip(*List)))

# a,b = [*(1,2)]  
# print(a,b)

# Equivalent the the code for zip
for u in zip(*[(1,2),(3,4),(5,6),(7,8),(9,10)]):
	print(u,end='   ')
