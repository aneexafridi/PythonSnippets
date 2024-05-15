from numpy import block

# help(block)

A  = block([['a','b'],['C','D']])
B  = block([['a','b'],['C','D']])
print(block([[A],[B]]))

