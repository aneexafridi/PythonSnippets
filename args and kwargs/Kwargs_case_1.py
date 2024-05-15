# Case 1

def Fun(**kwargs):
	print(kwargs)
	print('len',len(kwargs))
	print(type(kwargs))

Fun(a='A',b ='B')