from heapq import heappushpop

# help(heappushpop)

# if we need push and pop for heap then we should use 
# the combination of the two function like heappushpop

# Push item on the heap, then pop and return the smallest 
# item from the heap. The combined action runs more efficiently
# than heappush() followed by a separate call to heappop()

List = [1,2,3,4,5]
print(List)
print()

heappushpop(List,9) 
# the smallest element will be remove for list
# then new item insert into  list

print(List)

