# insert(i, x)
# Insert x into the deque at position i.

# If the insertion would cause a bounded deque to grow beyond 
# maxlen, an IndexError is raised.

from collections import deque

Deque = deque(['a','c','d'])
print(Deque)
print()

print('After insert the item specifi position')
Deque.insert(1,'b')
print(Deque)