# Cloning List
# Cloning() method
# we can clone a list into another list using Slicing.
# when we clone a list a separate copy of all the elements is store in another list.
# both the lists are independent.

# copy() method and cloning same work but way different
A = [1,2,3]
B = A[:]
print(A,id(A))
print(B,id(B))
print("After copy method use")
B[0] = 99
print(A,id(A))
print(B,id(B))

# Modification in a will not 
# affect b and vice versa