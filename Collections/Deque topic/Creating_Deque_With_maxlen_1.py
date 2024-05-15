from collections import deque
# help(deque)
# for the rule  "LIFO" Last in First out

# deque pronounced “deck” and is short for 
# “double-ended queue” and O(1) performance

Tuple = ('A','B','C')
DeQue = deque(Tuple,maxlen=3)
print(DeQue)

print(DeQue.maxlen)
# is property of the deque mean variable