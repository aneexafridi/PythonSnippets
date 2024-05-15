
A = int(input("Enter A: "))
B = int(input("Enter B: "))

try:
	C = A/B
except ArithmeticError:
	print("ArithmeticError sorry!!")
	
# except ArithmeticError as Arith:
# 	print(Arith)
else:
	print(C)
