from collections import deque

# help(deque.append)
# method add the element in to the deque from right side

List = [1,2,3]
Deque = deque(List)
print(Deque)

print()

Deque.append('Shahab')
Deque.append(38)
print('After append the data in to Deque')
print(Deque)