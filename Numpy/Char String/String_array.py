from numpy import char

List = list() # Empty list

Length = int(input("Enter the Length: "))
for _ in range(Length):
	List.append(input("Enter Name: "))

Char_Array = char.array(obj=List)
# char.array auto increase the size of the element 
print(Char_Array)
print(type(Char_Array))



