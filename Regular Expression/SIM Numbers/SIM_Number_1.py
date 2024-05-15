# explain r'' raw string read all character \t\n
# 03 must be at begining of the number
# [0-4]  mean 0 to 4  at third position must be one
# \d{N}  numbers must be >=N else no match
# \b is the boundary of pattern

from re import match

Test = match(pattern=r'03[0-4]\d{8}\b',string='03025509950')

if Test:
	print(Test.group())
else:
	print('Not Match')
