from queue import Queue

# help(Queue.full)

Q = Queue(maxsize=1)
print(Q.full())

Q.put('Equal')
print('After Put some data in Queue')
print(Q.full())
print('Now Queue is Full')
