# ----List Compreshension
# List Compreshension with iIf else Statement
# Syntax:---
# List = [expression if_statement else expression for u in iterable_object]

# Example
# List = [u if u%2==0 else "odd" for u in range(1,11)]

List_1 = [] # create Empty list
for u in range(1,11):
	if u%2==0:
		List_1.append(u)
	else:
		List_1.append("Odd")
print("List_1\n\t\t",List_1)

List_2 = [u if u%2==0 else "Odd" for u in range(1,11)]
print("List_2\n\t\t",List_2)