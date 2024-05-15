# ----List Compreshension
# List Compreshension with iIf else Statement
# Syntax:---
# List = [for u in iterable_object expression if_statement if_expression]

# Example
# List = [u for u in range(1,11) if u%2==0 if u%3==0]

List_1 = [] # create Empty list
for u in range(0,20):
	if u%2==0:
		if u % 3 ==0:	
			List_1.append(u)
print("List_1\n\t\t",List_1)

List_2 = [u for u in range(0,20) if u%2==0 if u%3==0]
print("List_2\n\t\t",List_2)

# both are same working