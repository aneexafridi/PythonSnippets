# always default argument must be after the standard parameter
# in this case standard argument is value
# and default argument is start

def Default_Arg_Val(value,start=0):

	return start+value


print(Default_Arg_Val(1))
print(Default_Arg_Val(1,9))