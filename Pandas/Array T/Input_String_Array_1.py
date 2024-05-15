# pandas array doesn't any method to add or append the data
# i use this method for input data like string
from pandas import array 
# help(array)

Length = int(input("Enter the Length of Array: "))
Names = array(range(Length),dtype='string')
print(Names)

for u in range(Length):
	Names[u] = input("Enter Name: ")
print("\n")

for name in Names:
	print(name)