# sort the keys and value both are sorted
Dict = {'B':4,'D':2,'C':1,'A':3}
print(Dict)

#note we can also descending order just 
# sorteds function(reverse=True)
keys = sorted(Dict.keys())
values = sorted(Dict.values())

# dictionary comprehension
Dict = dict({k:v for k,v in zip(keys,values)})
print('\nAfter sorted keys  and values')
print(Dict)