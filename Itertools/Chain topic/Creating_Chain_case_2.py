from itertools import chain

digits = (1,2,3,4)
alph = ('ABC','DEF')
names = ['khan','Afridi']
Conditions = [False,True]

Chainning = chain(digits,alph,names,Conditions)

print(''.join(map(str,Chainning)))


# str method is used for integers to convert into string

# --------------------------Note ------
# 		if we have single 
# List of tuple like [(),()] or List of List [[],[]]
# Tuple of List like ([],[]) or Tuple of Tuple ((),())

# Then we use asterisk * before the iterable
