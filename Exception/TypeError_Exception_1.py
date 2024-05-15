# 				exception TypeError
# Raised when an operation or function is applied to an
# object of inappropriate type. The associated value is 
# a string giving details about the type mismatch.

try:
	Add = "10"+5
except TypeError as type_error:
	print(type_error)
else:
	print(Add)