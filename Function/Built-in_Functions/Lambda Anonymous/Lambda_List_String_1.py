List = ['Python','java','JavaScript','Php','Html']
print(List)
print()
Convert_Upper = lambda x:str(x).upper()
print(Convert_Upper(List))

# if you may be thinking why we convert the x into str
# we known that x represent the each element in given List
# which is a string(element)
# because x as treated the object of list not as String element

# that's why need to convert list object into str
# ------------------------------------------------------
# print(' '.join(List).upper()) return string
# print([u.upper() for u in List]) return list
