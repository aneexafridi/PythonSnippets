from queue import Queue

# help(Queue.empty)

Q =  Queue()
print(Q.empty())
print()

print('After put some data in Queue')
Q.put('Equal')
print(Q.empty())

