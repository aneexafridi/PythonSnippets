from collections import OrderedDict

Dict = {'A':1,'B':2,'C':3,'D':4}
print(Dict)
print()

order = OrderedDict(Dict)

order.move_to_end(key='B',last=True)

print('After move to end')

for k,v in order.items():
	print(k,'=',v)

print('move the B key to last')
print(''.join(order.keys()))