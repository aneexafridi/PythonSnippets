# using zeros() function for input
from numpy import *
Row = int(input("Enter Row: "))
Colomn = int(input("Enter Colomn: "))
Zeros = zeros((Row,Colomn),dtype=int)
print("Created Zeros Array\n",Zeros)
for m in range(len(Zeros)):
	for n in range(len(Zeros[m])):
		Zeros[m][n] = int(input(f'{m}{n} index: '))
	print()
print("After Modify the Zeros Array")
print(Zeros)