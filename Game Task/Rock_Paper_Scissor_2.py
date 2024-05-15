from random import randint

while True:
	
	Rock = randint(1,20)
	Scissor = randint(1,20)
	Paper = randint(1,20)

	if Rock==Scissor:
		print("\n\n\tRock Winner:))")
		print(f'\n\n\tRock: {Rock} and Scissor: {Scissor}')
		break
	elif Paper==Rock:
		print("\n\n\tPaper Winner:))")
		print(f'\n\n\tPaper: {Paper} and Rock: {Rock}')
		break
	elif Scissor==Paper:
		print("\n\n\tScissor Winner:))")
		print(f'\n\n\tScissor: {Scissor} and Paper: {Paper}')
		break
	else:
		print("\tRock: = {r:2d}  Scissor: = {s:2d}  Paper: = {p:2d}".format(r=Rock,s=Scissor,p=Paper))