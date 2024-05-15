List = [chr(u+65) for u in range(6)]
Tuple = tuple(v+65 for v in range(6))

Dict = {u:v for u , v in zip(List,Tuple)}
print(Dict)

