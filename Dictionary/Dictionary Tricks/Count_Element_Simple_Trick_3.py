Word = [('a',1),('b',2),('a',4),('c',9),('b',1)]

print(Word)


Dict = {}
for k,v in Word:
	Dict.setdefault(k,[]).append(v)
# we setdefault empty list [] to values  if frequently keys are exist


print(Dict)