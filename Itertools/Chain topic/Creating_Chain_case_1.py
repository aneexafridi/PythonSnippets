from itertools import chain
# help(chain)

iterable = [('ABC','DEF'),(1,2,3),['khan','Afridi'],[True,False]]
#-------------------------------------------------
# print(''.join(iterable)) # direct
# this will give to us error because in iterabe
# list,tuple not same order
# need for join method same like [(),()],(()()),[[],[]],([],.)
#-------------------------------------------------
Chainning = chain(*iterable)
print(''.join(map(str,Chainning)))

# str method is used for integers to convert into string

# --------------------------Note ------
# 		if we have single 
# List of tuple like [(),()] or List of List [[],[]]
# Tuple of List like ([],[]) or Tuple of Tuple ((),())

# Then we use asterisk * before the iterable
# this will packing or unpacking
