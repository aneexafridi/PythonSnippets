# ----------------------enumerate() method
# this method return the tuple container,it useful for List or 
# iterable objects like tuple,List,String;


# help(enumerate)

Tuple = ("A","B","C","D")
print(Tuple)
print("\nPrint the Tuple Elements with Index")
# start is  by default  set  start=0
for u ,v in enumerate(Tuple,start=1):
	print(f'{u} = {v} ')
print("\nAnother Way")
for u in enumerate(Tuple,start=1):
	print(u)
print("\nFor String")
Name = "Equal"
print(Name)
for character ,index in enumerate(Name,start=0):
	print(f'{character} = {index}')