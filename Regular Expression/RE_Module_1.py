# >> match return Boolean value True if not match then None

# match method match at the begining of the string

#			search() vs. match()
# Python offers two different primitive operations based on 
# regular expressions: re.match() checks for a match only at 
# the beginning of the string, while re.search() checks for a 
# match anywhere in the string (this is what Perl does by default)


from re import match,search

L=search(pattern=r'03[0-4]\d{8}\b',string='abasdf03025509950')
if L:
	print(L.group())
else:
	print('\tNot match')