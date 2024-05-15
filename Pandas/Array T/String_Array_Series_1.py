from pandas import array
# help(array)

# Length = int(input("Enter the length: "))

# A = array(range(Length),dtype='string')
# print(A)
# for u in range(Length):
# 	A[u] = input("Enter Data: ")

# for u in A:
# 	print(u,end=' ')
A = array(['1',2],dtype='object')
print(A)
for u in range(2):
	if type(A[u])==int:
		print("Int value: ",A[u])
	elif type(A[u])==str:
		print("String value: ",A[u])
