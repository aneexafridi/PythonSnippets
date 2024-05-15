marks = 90
Roll = 38

Conditions = [
			  marks > 75,
			  Roll > 30
			  ]
# Condition list we can put muitple conditions
# all Function return only if and only if all condition True

if all(Conditions):
	print('Awesome')


# Equivalent Code the above

# marks = 90
# Roll = 38

# if marks>75 and Roll > 30:
# 	print("Awesome")
