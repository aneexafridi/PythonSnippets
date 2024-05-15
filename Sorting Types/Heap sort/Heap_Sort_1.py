from heapq import heapify,heappop

# heapify Function convert list into heap then
# inplace to the orignal List
# help(heapify)

# heappop return the pop the smallest element  from
# the heap 

# help(heappop)
List = [4,1,2,3]
print(List)
print('\nAfter transform the List into Heap')
heapify(List)
print(List)
print('\nAfter sorted')
# heappop method return smallest value in heap
# then store in List Comprehension
Sorted_List = [heappop(List) for _ in range(len(List))]
print(Sorted_List)