def Adding(A,B):
	if B==0:
		return A
	return Adding(A+1,B-1)
A = int(input("Enter A Value: "))
B = int(input("Enter B Value: "))
# try one line using unpacking way or procedure
print(f'Sum of {A} and {B} is: ', Adding(A,B))