# ------------random.choice(seq)
# Return a random element from the non-empty
# sequence seq.
# If seq is empty, raises IndexError.
from random import choice

def Show_Choise(Time,Object):
	for u in range(Time):
		print(choice(Object),end=" ,")

List = ["red","blue","yellow","green"]
Tuple = ("red","blue","yellow","green")
String_Name = "Equal!=equal"

print("------------List Data\n")
Show_Choise(5,List)
print("\n----------Tuple Data\n")
Show_Choise(5,Tuple)
print("\n----------------String Name\n")
Show_Choise(6,String_Name)