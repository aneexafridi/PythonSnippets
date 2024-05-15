from heapq import heappush,heappop
List = [1,4,2,3]
print(List)

Sorted = []
for u in List:
	heappush(Sorted,u)
Sorted = [heappop(Sorted) for _ in range(len(Sorted))]
print(Sorted)