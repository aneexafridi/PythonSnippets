from collections import deque

List = [1,2,3,2,2,3]
Deque = deque(List)
print(Deque)

print()

print('After the Count 3 in Deque: ',end='')
print(Deque.count(3))