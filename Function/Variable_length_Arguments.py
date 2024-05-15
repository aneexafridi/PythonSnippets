# Variable length arguments is an argument that can
# accept any number of values. the Variable length
# argument is written with * symbol
# It stores all value in a tuple

def Varible_length(*Var):
	# Sum = 0
	# for u in range(len(Var)):
	# 	Sum +=Var[u]
	print(f"The sum is {Var}") # for Sum remove Var from f-string

Varible_length(1,2,3,4)