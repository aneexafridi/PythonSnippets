# using Zeros() function for input
from numpy import*
Number = int(input("Enter Number of Elements: "))
Array_A = zeros(Number,dtype=int)
for u in range(Number):
	Array_A[u] = int(input(f'{u} Index: '))

print(Array_A)