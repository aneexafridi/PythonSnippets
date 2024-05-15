# -------Nested List Compreshension
List_1 = [] # created empty List
for u in range(1,3):
	for v in range(1,11):
		List_1.append(v)
print("List_1\n",List_1)

List_2 = [[u for u in range(1,11)] for v in range(1,3)]
print("List_2\n",List_2)