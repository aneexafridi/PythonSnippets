from collections import deque
# help(deque)
# for the rule  "LIFO" Last in First out

# deque pronounced “deck” and is short for 
# “double-ended queue” and O(1) performance

DeQue = deque([1,2,'ali',4,5])
print(DeQue)

DeQue = deque('Shahab')
print(DeQue)

print(DeQue.maxlen)
# is property of the deque mean variable