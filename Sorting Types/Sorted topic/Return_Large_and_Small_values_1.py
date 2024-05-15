List = [4,1,3,5,2]

print(List)
print('\n')

# return a new list 
# here we want small value in List
Small_value = sorted(List)[0]

print(f'{Small_value} is small value in The List')

# here we want small value in List
large_value = sorted(List)[-1]
print(f'{large_value} is large value in The List')