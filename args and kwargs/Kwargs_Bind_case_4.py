# case 4
def Fun(a,b,c):
	print(f'a: {a}\nb: {b}\nc: {c}')

kwargs ={'b':22,'c':33}

Fun(11,**kwargs) # 11 pass to a other remaining to others
