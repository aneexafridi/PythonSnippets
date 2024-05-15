from collections import Counter

Dict = {1:'a',2:'b',3:'a',4:'a',5:'b',6:'c'}
print(Dict)
print('\n')
# counting the dict values how many time occur the same key
Counter_object = Counter(Dict.values())
print(Counter_object)
print('\n')
print(Counter_object.most_common(3))