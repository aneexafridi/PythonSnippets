# case 3

def Fun(a,b,*args,c,d):
	print(a)
	print(b)
	print(args)
	print(c)
	print(d)

Fun('one','two','three','Four',c='Five',d='Six')
