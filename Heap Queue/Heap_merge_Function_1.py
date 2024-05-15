from heapq import merge
# help(heapmerge)


List_1 = [1,4,3]
List_2 = [2,6,5]

print(List_1)
print(List_2)


List =list(merge(List_1,List_2))
# pretty same like list built-in function like extend method
print('After merge the two LIsts')
print(List)

