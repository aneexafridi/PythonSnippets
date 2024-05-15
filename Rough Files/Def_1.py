def Yell(text):
	return text.upper()+"!"
print(Yell("Shahab"))
bar = Yell
print(bar.__name__)