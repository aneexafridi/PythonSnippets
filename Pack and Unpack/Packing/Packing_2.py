from re import split
String = ' 13.9a.3'
spliter = split(r'[^0-9.]+',String)
p = list(filter(lambda x:x!='',spliter))
print(spliter)
print(p)
L = lambda x:float(x) if '.' in x else int(x)
print(list(map(float,p)))
