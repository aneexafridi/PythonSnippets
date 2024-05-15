# List = [1,2,3,2,1,2,3,4,2,3,2,5,2,3,2]
List = [2,2,2,2,4,5,5,1,5,5,3,5]
print(List)
Most_occur = max(map(List.count,set(List)))




for u in set(List):
	if List.count(u) == Most_occur:
		print(u)

b = lambda x:(x if x>8 else '')
print(b(8))

# print(f'{List.count(7)} Most occur element in the List {Most_occur} Times')

# print('\n')

# print("Most occur: ",List[Most_occur])
# print("Most occure element Time: ",Most_occur)
# # 
# Explain each part of the code particular of the line NO 4
# set(List) set Function return = {1,2,3,4,5} unique element of List
# List.count method apply for counting the each element in set(List)
# map Function return the object which is [1,4,5,3,1]
#then apply max Function in the Map Function to get the maximum number 5
# then getting the value most occurence in the list -> List[Most_occur] 3
