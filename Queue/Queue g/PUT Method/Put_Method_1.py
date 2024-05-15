from queue import Queue
from threading import Thread

# help(Queue.put)
Q = Queue()
def Worker():
	while True:
		item = Q.get()
		print(f'Workeing on {item}')
		print(f'Finished {item}')
		Q.task_done()

T = Thread(target=Worker,daemon=True)
T.start()

for item in range(30):
	Q.put(item)
print('All task requests set\n',end='')
Q.join()
print('All work completed')
