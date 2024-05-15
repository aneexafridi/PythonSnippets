from secrets import choice
from string import ascii_letters,digits

Alphabets = ascii_letters + digits

# choice method is import from random module in secrets module

Password = ''.join(choice(Alphabets) for _ in range(8))

print(Password)

print('\nComprehension')
Compreshension =   '|'.join(u for u in ['Anees','Bilal','Shahab'])
print(Compreshension)