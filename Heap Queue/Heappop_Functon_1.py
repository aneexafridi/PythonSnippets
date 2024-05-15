from heapq import heappop ,heapify
# help(heappop)

# heappop - This fucntion returns the smallest data element from
# the heap.

List = [1,4,3,2,9,5]

print(List)

heapify(List)
# Convert regular List into heap

print(List)

pop = heappop(List)

print('After pop the heap: ',pop)
print(List)

