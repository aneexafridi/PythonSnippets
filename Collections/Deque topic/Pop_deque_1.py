from collections import deque

# help(deque.pop)

List = [1,2,3,4]
Deque = deque(List)
print(Deque)
print()
print('After pop method')
print(Deque.pop())
print(Deque)