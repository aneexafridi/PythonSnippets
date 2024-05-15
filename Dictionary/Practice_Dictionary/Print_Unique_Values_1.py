# print all unique values in a Dictionary
List = [{"v":"SOO1"},{"v":"SOO2"},{"vl":"SOO1"},
{"vl":"SOO5"},{"vll":"SOO5"},{"v":"SOO9"},{"vlll":"SOO7"}]
print(List)
Set = set() # created Empty set
for u in List:
	Set.update(u.values())
# Set.update method return multiple elements
print("Unique Values")
print(Set)