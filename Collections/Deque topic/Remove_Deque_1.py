# remove(value)
# Remove the first occurrence of value. 
# If not found, raises a ValueError.

from collections import deque

Deque = deque([1,2,3,4])
print(Deque)

print('After remove the specific value from deque')
Deque.remove(3)
print(Deque)