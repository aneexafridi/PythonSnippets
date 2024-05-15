# all Argument must be
# integers,where its positve or negative
# you can not pass a string or float number or 
# any other type in a start,stop and stepsize
# The stepsize should be not zero
# Example:  range(start,end,step) "end" exclude
# Range  = range(1,5)
# for r in Range:
# 	print(r,end=' ')
Name = "Afridi"
Name_length = len(Name)
for u in range(Name_length):
	print(u,"=",Name[u])