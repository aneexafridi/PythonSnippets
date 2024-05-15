from array import*
Dict = {'1':['a','b'],'2':['c','d']}
Array = array('u',[])
print(Dict)
for value in Dict.values():
	for v in value:
		Array.append(v)
for u in range(2):
		print(f"{Array[u]}{Array[2+u]}")



# L1 = Dict["1"]
# L2 = Dict["2"]
# for u in range(2):
# 	for v in range(2):
# 		print(f"{L1[u]}{L2[v]}")



19
import itertools      
d ={'1':['a','b'], '2':['c','d']}
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))
	


L = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",L)
u_value = set( val for dic in L for val in dic.values())
print("Unique Values: ",u_value)


from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)
