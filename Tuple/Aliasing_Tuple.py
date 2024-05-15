# --------------Aliasing Tuple
# Aliasing means giving another name to the existing object.
# It doesn't mean copying.

A = (1,2,3,'A',4)
B = A
print(A,id(A))
print(B,id(B))
