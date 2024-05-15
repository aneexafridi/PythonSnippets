# Global keyword
# If local variable and global variable has same
# name then the functiion by default refers to
# the local variable and ignores the global variable.

# It means global variable is not accessible inside the
# function but possible to  access outside of function

# In this situation, If we need to access global variable
# inside the function we can access it using global keyword
# followed by variable name

# G = 100
# def Display():
# 	global G
# 	G = G+99
# 	print("Global G",G)
# Display()
# print("Global G",G)

g = 0
def Iterator():
	global g
	while g<11:
		g+=1
		print(g,end=' ')
Iterator()
print("\nGlobal g: ",g)