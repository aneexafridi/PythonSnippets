# syntax Ones
#  Ones((shape),dtype=float,order='C')
# note --- Shape in open ()
from numpy import *
Ones = ones((3,3),dtype=int)
print(Ones)
print("Accessing by loops")
for m in range(len(Ones)):
	for n in range(len(Ones[m])):
		print(Ones[m][n],end=' ')
	print()
# without Accessing indexes
# for m in Ones:
# 	for n in m:
# 		print(n,end=' ')
# 	print()

