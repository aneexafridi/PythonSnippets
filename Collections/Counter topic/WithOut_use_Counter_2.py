List = [1,4,3,2,1,1,1,3,1,5,1,1,2,1,4]

print(List,'\n')
Set = set(List)
Elements = [List.count(u) for u in Set]
# List Comprehension return the list

print(Elements)

Zip_list= zip(Elements,range(1,len(Elements)+1))

Element = max(Zip_list)[1]

Time_occur = max(Elements)
print(f'Frequently occur Element in List: {Element}')
print(f'Time occur: {Time_occur}')