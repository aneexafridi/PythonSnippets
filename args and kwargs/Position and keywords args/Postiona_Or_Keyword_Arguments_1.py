# -------------- Positional-or-Keyword Arguments
# If / and * are not present in the function definition, 
# arguments may be passed to a function by position or by keyword.

def Standard(arg):
	print(arg)

# both will be accepted
Standard(arg='Equal')
Standard('equal')
