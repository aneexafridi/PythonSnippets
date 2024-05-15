# ZeroDivisionError :
# this the sub class of the ArithmeticError

try:
	D = 4/0
except ZeroDivisionError as zero_division_error:
	print(zero_division_error)