from statistics import mode
# help(mode)

List = [1,2,3,1,2,4,5,2]
print(List)

print(f'Mode: {mode(List)}')

print()

# when  no iterable object have repeated element
# then return the first index element
List = [3,2,1]
print(List)
print(f'Mode: {mode(List)}')