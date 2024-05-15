# Counter object follow some "Common patterns"
# like clear(),values(),items() 
# and also convertion list,dict,tuple
from collections import Counter

Tuple = ('c','a','b','c','d','a','b','a')
print(Tuple) 
Counter_object = Counter(sorted(Tuple))

print(Counter_object)
for k,v in Counter_object.items(): 
	print(k,' = ',v)
