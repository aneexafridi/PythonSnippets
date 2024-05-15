Length = int(input("Enter the length of Tuple: "))

List = [] # created Empty list

for u in range(Length):
	List.append(input("Enter: "))	

print("List\n",List)
Tuple = tuple(List)
print("Tuple\n",Tuple)