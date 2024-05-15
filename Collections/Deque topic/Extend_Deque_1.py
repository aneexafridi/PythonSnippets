from collections import deque

Deque_A = deque((1,2,3,4))
print("A: ",Deque_A)
Deque_B = deque((5,6,7,8))
print("B: ",Deque_B)

print()
print('After the Extend the Deque_B to Deque_A')

Deque_A.extend(Deque_B)

print(Deque_A)