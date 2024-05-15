# -------------------Queue(maxsize=0)
# Constructor for a FIFO queue. maxsize is an integer that sets
# the upperbound limit on the number of items that can be placed
# in the queue. Insertion will block once this size has been reached,
#  until queue items are consumed. If maxsize is less than or equal
#  to zero, the queue size is infinite.
# FIFO ->> First In First out

from queue import Queue

Q = Queue() # default = 0 which mean we can insert infinite
print(Q)

