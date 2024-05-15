# Two dictionaries combine adding the values
# if the keys are same else update

Dict_1 = {'a':30,'b':20,'c':10}
Dict_2 = {'a':60,'b':50,'d':40}
print(Dict_1)
print(Dict_2)
Dict_3 = {}
for u ,v in Dict_1.items():
	for m,n in Dict_2.items():
		if(u==m): # checking keys Dict_1 == Dict_2
			Dict_1[u] = v+n
		else: # else update the Dict_3
			Dict_3 = {m:n}
			
Dict_1.update(Dict_3)
print(Dict_1)


from collections import Counter
Dict_1 = {'a':30,'b':20,'c':10}
Dict_2 = {'a':60,'b':50,'d':40}
print(Dict_1,'\n',Dict_2)
C = Counter(Dict_1) + Counter(Dict_2)
print(C)
























