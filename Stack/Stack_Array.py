from array import*
Length = None
Array = array('i',[])

def Insert(insert_data):
	Array.append(insert_data)
def Pop():
	Array.pop()
Insert(44)
print(Array)
Pop()
print(Array)