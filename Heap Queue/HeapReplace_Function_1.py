from heapq import heapreplace
# help(heapreplace)

# heapreplace- This function replaces the smallest data element with a new
# value supplied in the function
# Pop and return the smallest item from the heap,
# and also push the new item. The heap size doesn’t change.
# If the heap is empty, IndexError is raised.

List = [1,4,3,2,9,5]

print(List)

Replace = heapreplace(List,100)

print('After heapreplace data in the List',Replace)
print(List)

