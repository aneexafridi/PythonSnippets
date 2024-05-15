from queue import Queue

Q = Queue()

Q.put(8)
Q.put(9)
print("Size: ",end=' ')
print(Q.qsize())

print(Q.get(False))
print("Size: ",end=' ')
print(Q.qsize())

