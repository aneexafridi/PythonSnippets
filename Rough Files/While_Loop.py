number = 1
while number<=200:
	if number%3==0 and number%5==0:
		print("Pizz+Bazz",end=" ")
	elif number%3==0:
		print("Pizz",end=" ")
	elif number%5==0:
		print("Bazz",end= " ")
	else:
		print(number,end=" ")
	number+=1

print("\n\t\t\t\t\t\t\tDone :)")
print("\n\n\n\n")