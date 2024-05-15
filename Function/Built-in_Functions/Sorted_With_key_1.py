List = [5,3,42,4,1]
print(List)

print()
print(sorted(List,key=lambda x: 0 if x==42 else x))

