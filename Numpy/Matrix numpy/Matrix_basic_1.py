from numpy import matrix

print(matrix(data='1 2;3 4')) # way 1
print('\n')
print(matrix(data='1,2;3,4')) # way 2
print('\n')
print(matrix(data=([1,2],[3,4]))) # way 3
print('Transpose')
print(matrix(data=([1,2],[3,4])).T)