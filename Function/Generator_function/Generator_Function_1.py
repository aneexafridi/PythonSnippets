# --------Generatar
# Generatars are functions that return a sequence of values.
# we use "yield" Statement to return the value from function.

# -------- yield Statement
# yield statement returns the element from a generator function
# into a generator object.
#    Example:-- yield a 

# -------- Next() function
# This function is used to retrieve element by element from a
# generator object.
# Syntax:- next(generator_object)

# below generator function
def Show(a,b):
	while a<=b:
		yield a # return a value
		a+=1

Result = Show(1,10)
# and we can store list variable the result of generator function
print(list(Result))

# # next Function 
# print(next(Result)) # output 1
# print(next(Result)) # output 2

# for u in Result: # here result = 3 or next()
# 	print(u)


