# The Keyword variable length Argument wire with **Argument
# Note ---- key must be in the qoution
def Add(**Var):
	Sum = Var['a']+Var['b']+Var['c']
	print("Sum is",Sum)
Add(c=4,a=1,b=3)