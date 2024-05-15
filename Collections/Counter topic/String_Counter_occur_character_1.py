from collections import Counter

Name = 'Equal!=equal'
print(Name)

Counter_object = Counter(Name)
print(Counter_object)

print('occurrence counting in Name')
for k,v in Counter_object.items():
	print(k,' = ',v)