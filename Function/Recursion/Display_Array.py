from array import *
A = array('i',[1,22,3,4,5])

def Recur(a):
	if(a==0):
		return 0
	print(A[len(A)-a],end=' ')
	return a+Recur(a-1)
Recur(len(A))