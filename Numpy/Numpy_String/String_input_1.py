from numpy import char

Length = int(input("Enter the Length of Array: "))

List = []
print(List)
print()

for _ in  range(Length):
	List.append(input("Enter Element: "))

Chars = char.array(obj=List)

print(Chars)