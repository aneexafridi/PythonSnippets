#                  ValueError
# Raised when an operation or function receives an
# argument that has the right type but an inappropriate
# value, and the situation is not described by a more
# precise exception such as IndexError.

try:
	A = int(input("Enter number: "))
except ValueError:
	print("TypeError sorry!!")
else:
	print(f'you entered {A}')