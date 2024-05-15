from heapq import *
from sys import exit

class Heap_Queue(object):
	List = []
	@classmethod
	def Create_Heap(cls):
		heapify(cls.List)
	@classmethod
	def Push(cls,List,Item):
		heappush(cls.List,Item)
	@classmethod
	def Pop(cls):
		heappop(cls.List)

	@classmethod
	def Replace(cls):
		heapreplace(cls.List,item)
	@classmethod
	def Push_Pop(cls):
		heappushpop(cls.List,item)
	@classmethod
	def Show_List(cls):
		print(cls.List)

while True:
	H = Heap_Queue()
	User =int(input('''\tEnter [1] for Create Heap
   	Enter [2] for Heappush item
   	Enter [3] for HeapPop item
   	Enter [4] for HeapReplae item
   	Enter [5] for HeapPushPop
   	Enter [6] for See the List
   	Enter [7] for exit!!
   	>> '''))
	if User == 1:
		H.Create_Heap()
	elif User == 2:
		item = int(input("Enter element: "))
		H.Push(Heap_Queue.List,item)
	elif User == 3:
		H.Pop()
	elif User == 4:
		R = int(input("Enter Replce Item: "))
		H.Replace(H.List,R)
	elif User == 5:
		P = int(input("Enter Push and Pop: "))
		H.Push_Pop(H.List,P)
		H.Push_Pop(H.List,)
	elif User == 6:
		H.Show_List()
	elif User == 7:
		print("Program is terminate:)")
		exit(0)
	else:
		print("Invalid Entered")
