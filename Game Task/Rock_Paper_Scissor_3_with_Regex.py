from random import *
import re as RE

List = ["Rock","Scissor","Paper"]
def Checking(User):
	if RE.fullmatch("[RSP][a-z]+",User) is not None:
		return  True
	else:
		return False
lelt = 5

########Sound__!=__Sound#########

for i in range(5):
	lelt-=1
	Ran = randint(0,2)
	User = input("Now Enter: ")
	if Checking(User):
		if List[Ran] == "Paper" and User == "Scissor":
			print("You Win!!\n")
		elif List[Ran] == "Rock" and User == "Paper":
			print("You Win!!\n")
		elif List[Ran] == "Scissor" and User == "Rock":
			print("You Win!!\n")
		else:
			print("Computer Win!!!\n")
	else:
		print("invalid Input ((:\n")
	print("chance lelt: ",lelt)

print("\nGame over!!!!\n")