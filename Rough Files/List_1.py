symbols = "ABCDZ"
code=[]
for symbol in symbols:
	code.append(ord(symbol))
for u in range(len(symbols)):
	print(code[u],end=", ")