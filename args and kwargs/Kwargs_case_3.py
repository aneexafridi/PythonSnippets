# case 3
def Fun(**kwargs):
	# items() method of dictionary which is return the object of dictionary class
	for key,value in kwargs.items(): 
		print(f'key: {key} Value: {value}')

Fun(c=33,d=44)