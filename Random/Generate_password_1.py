from random import *
password_length = int(input("Enter the length of password: "))
Alphabets = tuple(chr(c) for c in range(65,91))
j = "".join(sample(Alphabets,password_length))
print(j)