from collections import deque

List = [1,2,3,4]
Deque = deque(List)
print(Deque)

print()

Deque.appendleft(99)
print('After insert the item into deque from left side')
print(Deque)