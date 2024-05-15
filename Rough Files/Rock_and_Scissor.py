import random as Ran

while True:
	Rock = Ran.randint(1,20)
	Scissor = Ran.randint(1,20)
	if Rock==Scissor:
		print("\nGame over!!!")
		print(f'Rock: {Rock} and Scissor: {Scissor}')
		break
	else:
		print(f'Rock: {Rock} and Scissor: {Scissor}')