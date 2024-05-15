Length = int(input("Enter the length: "))
Dict={} # created empty Dictionary
for u in range(1,Length+1):
	Dict.setdefault(f'{u}',u*u) # use f'{u}' for string keys
	# Dict.update({u:u*u})
print(Dict)