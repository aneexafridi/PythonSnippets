#  Set = {} this is not empty set, this is dictionary
#  we can use set() method for empty Set
Set = set()
print("Memory location before entered Elements",id(Set))
Lenght = int(input("Enter the length of Set: "))
for u in range(Lenght):
	Set.add(input("Enter the Elements: "))

print("Display All the elements of Set")
print(Set)
print("Memory location After entered Elements",id(Set))