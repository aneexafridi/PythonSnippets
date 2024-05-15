from numpy import random,arange

help(random.permutation)
# # see the permutation decomentation
# # permutation meaning in dictionary {change the order}
# # as like the shuffle method in numpy
my_permute = random.permutation(10)
print(my_permute)
print('\n')
my_permute = random.permutation([11,22,33,44])
print(my_permute)

print('\n')

x = arange(1,10).reshape((3,3))
my_permute = random.permutation(x)
print(my_permute)
# --------------Note ------------------------
# also see the itertools library permutations topic