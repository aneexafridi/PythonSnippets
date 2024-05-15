from collections import Counter

Characters = list('abcabdcba')
print(Characters)
print('\n')
Counter_object = Counter(Characters)
print(Counter_object)
print('Sum of Values: ',end='')
print(sum(Counter_object.values()))