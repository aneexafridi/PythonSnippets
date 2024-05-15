# case 1
def Fun(*args):
	print(args)
	print(len(args))
	print(type(args))

Fun([1,2,3,4],5)
Fun(5,[1,2,3,4])