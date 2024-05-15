from random import choice
Guess = ('Rock','Paper','Scissor')

for u in range(3):
	computer = choice(Guess)
	user = input('Enter: ').title()
	if computer == user:
		print('Tie or Draw')
	elif computer == 'Rock' and user == 'Paper':
		print('User Win!')
	elif computer == 'Paper' and user == 'Scissor':
		print('User Win!')
	elif computer == 'Scissor' and user == 'Rock':
		print('User Win!')
	elif user not in Guess:
		print("Invalid")
	else:
		print("computer Win!")