# when we create  function to pass two or more arguments then
# We are getting surprisingly getting this Syntax Error
#----------------------------below---------------------------
# SyntaxError: non-default argument follows default argument

# this is because when passing the order of arguements of function
# in  Default argumet first and then Non-Default after
# That's why this happens occurrs often times for news programmers
# 
# def Sum(x=100,y):
# 	print(x+y)
# Sum(4)

# To fix this ugly Error see the below the Same function
def Sum(y,x=100):
	print(x+y)
Sum(4)
#Sum(4,5)