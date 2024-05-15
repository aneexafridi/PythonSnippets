from heapq import heapify,heappop
# help(heapify)

# Transform list x into a heap, in-place, in linear time.
# heapify([x]) = The Function converts a regular list to  heap.
# IN the resulting heap the smallest element
# gets pushed to the index position 0.But rest of the data
# element are not necessarily sorted

List = [1,4,3,2,9,5]

print(List)

heapify(List)

# heapify method used to alread list defined with some values

print(List)

pop = heappop(List)

print('After pop the heap: ',pop)
print(List)


