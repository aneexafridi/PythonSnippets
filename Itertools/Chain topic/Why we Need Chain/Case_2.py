from itertools import chain
#  case---2
List = [('a'),['b'],'c']

# print(''.join(List))
# print(''.join(Tuple)) 
# give error for not same order object
# join method does not concatenate like the List
# direct join method does not work to that chain

print(''.join(chain(*List)))
