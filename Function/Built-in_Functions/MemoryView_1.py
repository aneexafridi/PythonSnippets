# help(memoryview)

# memoryview is Class and some useful methods like tolist method etc.


M = memoryview(b'AZaz').tolist()
print(M)


print()

M = memoryview(b'!#$').tolist()
print(M)