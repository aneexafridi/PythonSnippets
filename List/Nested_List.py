# ----------------Nested List
# A list within another list is called as nested list
# or Nested of a list

A = [1,2,3,[44,55]]
print(A)
print(A[3]) # [44,55]
print(A[3][0]) # [44]
print(A[3][1]) # [55]
B = [3,4]
C = [1,2,B]
print(C)

D = [[1,2,3],
	[4,5,6]]
print(D)