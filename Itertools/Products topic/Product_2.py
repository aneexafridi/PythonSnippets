from itertools import product
A = [1,2]
print(f'A: {A}\n')

print('cartesian  product')

Result = product(A,repeat=3)
# repeat 3 mean A*A*A = [1,2],[1,2],[1,2] then cordition product role
print(tuple(Result))