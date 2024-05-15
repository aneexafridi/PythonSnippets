# Copying Tuple
# we can copy elements of tuple into another tuple using slice.

A = (1,2,3,4)
B = A[0:]
# if same data store in B then copy
print(A,id(A))
print(B,id(B))

# if data not same data copy in B
B = A[2:]
print(A,id(A))
print(B,id(B))