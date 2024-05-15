from itertools import product


A = [1,2]
B = [3,4]
print(f'A: {A} and B: {B}\n')

print('Cordition product')

Result = tuple(product(A,B))

print(Result)
