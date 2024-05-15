# Aliasing List
# Aliasing means giving another name to the existing object.
# It doesn't mean copying.
A = [1,2,3]
B = A
print(A,id(A))
print(B,id(B))
B[0] = 99
print(A,id(A))
print(B,id(B))
# Modification in a will affect b and vice versa.