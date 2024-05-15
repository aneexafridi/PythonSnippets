from statistics import mode
# help(mode)

List = ['A','B','C','A','B','C','B','D']
print(List)

print(f'Mode: {mode(List)}')

print()

# when  no iterable object have repeated element
# then return the first index element
List = ['c','b','a']
print(List)
print(f'Mode: {mode(List)}')