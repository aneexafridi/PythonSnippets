# Getting input from user into Dictionary
Length = int(input("Enter the Length of Dictionary: "))
Dict = {} # created Empty Dictionary
print(Dict)
for u in range(Length):
	key = input("Enter key: ").strip()
	value = input("Enter value: ").strip()
	# Dict.update(key:value)
	Dict.setdefault(key,value) # both will work fine
print("\nAfter Insertion the data into Dictionary")
print(Dict)