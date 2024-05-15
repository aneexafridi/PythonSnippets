# Case 4
def Fun(a,b):
	# print(str(a)+str(b))
	print(a+b)

# the effect of using the * operator on an argument when
# calling a function is that of unpacking the list or
# tuple argument

a = [[1],[2]] #just add two list result is [1,2]
# a = [1,2]
Fun(*a)

b = (3,4)
Fun(*b)







