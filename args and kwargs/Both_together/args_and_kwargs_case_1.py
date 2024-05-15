# case 1
def Fun(*args,**kwargs):
	print(args)
	print(kwargs)

Fun(1,2,33,44,55)
# kwargs create empty dictionary for us
# becase we does not pass any postional actual value

