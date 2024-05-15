from queue import Queue

# help(Queue.qsize)

Q = Queue()
Q.put('Equal')
Q.put('!=')
Q.put('equal')

print('The Size of Queue is: ',end='')
print(Q.qsize())