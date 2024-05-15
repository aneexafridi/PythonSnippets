		# why we need chain

from itertools import chain
#  case---1
Tuple = (('a'),['b'],'c')

# print(''.join(Tuple)) 
# give error for not same order object
# join method does not concatenate like the Tuple
# direct join method does not work to that chain
print(''.join(chain(*Tuple)))
