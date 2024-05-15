from heapq import*
List = []

while True:
	User =int(input('''\tEnter [1] for Create Heap
   	Enter [2] for Heappush item
   	Enter [3] for HeapPop item
   	Enter [4] for HeapReplae item
   	Enter [5] for HeapPushPop
   	Enter [6] for See the List
   	Enter [7] for exit!!
   	>> '''))
	if User == 1:
		heapify(List)
		print("Created")
	elif User == 2:
		item = int(input("Enter element: "))
		heappush(List,item)
	elif User == 3:
		if len(List) == 0:
			print("Heap is Empty")
		else:
			print('Pop',heappop(List))
	elif User == 4:
		R = int(input("Enter Replce Item: "))
		heapreplace(List,R)
	elif User == 5:
		P = int(input("Enter Push and Pop: "))
		heappushpop(List,P)
	elif User == 6:
		print(List)
	elif User == 7:
		print("Program is terminate:)")
		exit(0)
	else:
		print("Invalid Entered")