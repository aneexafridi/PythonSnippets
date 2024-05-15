# Case 6
Dict = {
		'1': 'one',
		'2': 'Two',
		'3': 'Three'
		}
# in this case must create dicd keys in string
# otherwise we will get error

def Fun(**kwargs):
	print(kwargs)
	print('len',len(kwargs))
	print(type(kwargs))


Fun(**Dict)