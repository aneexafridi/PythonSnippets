from collections import Counter

Counter_1 = Counter({'a':1,'b':2,'c':3})
Counter_2 = Counter({'d':4,'b':5,'e':7})
print(Counter_1)
print(Counter_2)
print('\t\t\tCounter_1 + Counter_2')
print(Counter_1+Counter_2)
print('\n')
Counter_1 = Counter(a=10,b=20)
Counter_2 = Counter(a=5,b=10)
print(Counter_1)
print(Counter_2)
print('\t\t\tCounter_1 + Counter_2')
print(Counter_1+Counter_2)