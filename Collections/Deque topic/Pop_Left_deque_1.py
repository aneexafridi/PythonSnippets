from collections import deque
# help(deque.leftpop)

# remove the item from left side of the deque
List = ['a','b','c','d']
DeQue = deque(List)
print(DeQue)
print()

print('After pop from left side of the deque')
print(DeQue.popleft())
print(DeQue)