from collections import deque

# help(deque.rotate)
# default set 0
Deque = deque([1,2,3,4,5])
print(Deque)
print('After rotate by 1')
Deque.rotate(1)
print(Deque)
print()

print('After rotate by 2')
Deque.rotate(2)
print(Deque)

print()

print('After rotate by 3')
Deque.rotate(3)
print(Deque)