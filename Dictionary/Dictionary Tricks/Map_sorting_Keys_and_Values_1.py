Dict = {'B':4,'D':2,'C':1,'A':3}
print(Dict)

keys = Dict.keys()
values = Dict.values()
#note we can also descending order just sorteds function(reverse=True)
Dict = dict(map(lambda k,v:(k,v),sorted(keys),sorted(values)))

print('After sorted keys and values')
print(Dict)

#  map(function lambda ,iterabble_1= keys,iterable_2= values)
# this map function take lambda function which is take two parameter
# which convert to tuple (k,v)
# and map function return the list of tuples like [(k,v),(k,v)]
# --------------------Note-------------------------
# built-in dict function take parameters only
# >> mapping=data like (a=10,b=20)
# >> **kwargs, and Tuples in list [(),()] or Tuples in tuple ((),())
# and some orthers




