import random as ra
import re as RE

List = ["Rock","Scissor","Paper"]
def Checking(User):
	if RE.fullmatch("[RSP][a-z]+",User) is not None:
		return  True
	else:
		return False
lelt = 5
for i in range(5):
	lelt-=1
	User = input("Now Enter: ")
	if Checking(User):
		if ra.choices(List) == "Paper" and User == "Scissor":
			print("You Win!!\n")
		elif ra.choice(List) == "Rock" and User == "Paper":
			print("You Win!!\n")
		elif ra.choice(List) == "Scissor" and User == "Rock":
			print("You Win!!\n")
		else:
			print("Computer Win!!!\n")
	else:
		print("invalid Input ((:\n")
	print("chance lelt: ",lelt)

print("\nGame over!!!!\n")