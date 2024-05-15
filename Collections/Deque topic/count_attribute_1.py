from collections import deque

# help(deque.count)

# if data no found then count method return 0

Name = 'Shahab'
Deque = deque(Name)
print(Deque)
print('count {a}: ',Deque.count('a'))

Tuple = (1,2,1,3,1,2)
Deque = deque(Tuple)
print(Deque)
print('count: {1} ',Deque.count(1))





