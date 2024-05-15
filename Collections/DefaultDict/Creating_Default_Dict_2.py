from collections import defaultdict

Word = "Colonel"
print()
print('\t'*10,Word)

Dict = defaultdict(int)  # default value pass "int"

for k in Word:
	Dict[k] +=1

print(Dict)