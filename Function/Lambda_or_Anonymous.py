# Anonymous Function or Lambda
# lambda function return multiple expressions

# Syntax:- lambda argument_list: expresion

Anonymous = lambda x,y: (x+y, x-y)
add , subtract = Anonymous(3,2)
print(add)
print(subtract)

printing = lambda x: print(x)
printing("Hi")

# default argument
Sum = lambda x,y=10:x+y
print("Default argument: ",Sum(4))
print(Sum(3,4))
