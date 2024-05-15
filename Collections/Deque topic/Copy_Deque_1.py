from collections import deque

Deque_a = deque(('Shahab','Afridi'))
print(Deque_a)
print(f'Id of Deque_a: {id(Deque_a)}')
print()

print('After Copy the data from Deque_a to Deque_b')
Deque_b = Deque_a.copy()

print(Deque_b)
print(f'Id of Deque_b: {id(Deque_b)}')
# ----------------------------Note-------------------------
# Deque_b = Deque_a.copy()   is not equal to Deque_b to Deque_a
# because  that statement create the new memory  for Deque_b