# -----------------Dot Function
# 	Noneumpy.dot(a, b, out=None)
# 	Dot product of two arrays. Specifically,
# a and b both are array type whether 1_d or ndarray

from numpy import dot

print('Multplication of two arrays')
a = [[1, 0],
	[0, 1]]
print(a)
b = [[4, 1],
	[2, 2]]
print(b)
print('\n')
print(dot(a, b))

print(dot(2,3))