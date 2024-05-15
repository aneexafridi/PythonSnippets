# Nested Dictionary

Dict = {1:"one",2:"two",3:"three",4:{4:"four",5:"five"}}
print(Dict)
# access by key various way we can do


for key ,value in Dict.items(): # items() method return Tuple
# checking the value is Dictionary or not
	if type(Dict[key]) is dict: 
		for key_1,value_1 in Dict[key].items():
			print(key_1,value_1)
	else:
		print(key,value)
