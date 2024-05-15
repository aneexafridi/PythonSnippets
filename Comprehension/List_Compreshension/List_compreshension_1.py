# --------------List Comprehension
# List Comprehension represents creation of new list from
# an iterable object that satisfy a given condition.
# Syntax:--
		# List_Name= [expression for item in iterable_object if_statement]
		# There can be zero or more if_Statement
		# There can one or multiple for loops.
		# Examples
		# List_1 = [i+1 for i in range(20)]
		# List_2 = [i for i in range(20) if i%2==0]
		# List_3 = [i for i in range(20) if i%2==0if i%3==0]

List_1 = [] # create empty list
for u in range(1,11):
	List_1.append(u)
print(List_1)

List = [u for u in range(1,11)]
print(List)
# both are Same