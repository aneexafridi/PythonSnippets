# syntax Zeros
#  zeros((shape),dtype=float,order='C')
# note --- Shape in open ()
from numpy import *
Zeros = zeros((3,3),dtype=int)
print(Zeros)
print("Accessing by loops")
for m in range(len(Zeros)):
	for n in range(len(Zeros[m])):
		print(Zeros[m][n],end=' ')
	print()
# without Accessing indexes
# for m in Zeros:
# 	for n in m:
# 		print(n,end=' ')
# 	print()

