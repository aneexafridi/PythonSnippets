# note tuple compreshension is not  exist in current python
# we should be convert the generator object into tuple object
# like below two Tuples
# Tuple = (u for u in range(1,10))
# print(Tuple)





Tuple = tuple(x for x in range(1,11))
print(Tuple)
# for even numbers

Tuple = tuple(x for x in range(1,11) if x%2==0)
print(Tuple)
