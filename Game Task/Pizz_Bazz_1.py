# Pizz and Bazz game
# Rules 
# 1 >> if number divide by 3 and 5 then Pizz + Bazz
# 2 >> if number divide by 3 then Pizz
# 3 >> if number divide by 5 then Bazz

while True:
	user = int(input("Enter any number: "))
	if user%3==0 and user%5 == 0:
		print('Pizz_Bazz')
		break
	elif user%3==0:
		print('Pizz')
		break
	elif user%5==0:
		print('Bazz')
		break
	else:
		print('not divided by these')
