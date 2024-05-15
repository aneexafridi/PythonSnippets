from queue import Queue

Q = Queue(maxsize=2)
List = [1,2,3,4]
Q.put(List)
print(Q.get())

print(Q.qsize())
