from secrets import choice
from string import ascii_letters,digits
alphabet = ascii_letters + digits
while True:
    password = ''.join(choice(alphabet) for i in range(10))
    if (any(c.islower() for c in password)and any(c.isupper() for c in password) and sum(c.isdigit() for c in password) >= 3):
    	print('currect password')
    	print(password)
    	break
    print(password)

# password should contain at least 3 digits and at least one small character
