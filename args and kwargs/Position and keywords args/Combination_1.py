# (Postion or keyword) argument and (positonal_only_arg) and (keyword_only_parameter)


def Combine(p,/,standard,*,keyword):
	print(p)
	print(standard)
	print(keyword)

#keyword must write and standard write or not and p never write in parameter

Combine('Equal',standard='!=',keyword='equal') 
print('\n')
Combine('Equal','!=',keyword='equal')