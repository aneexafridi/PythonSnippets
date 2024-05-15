# You have two dictionaries and want to find out
# what they might have in common (same
# keys, same values, etc.)

A = {'a':1,'b':4,'c':3}
B = {'d':9,'c':2,'f':1}
print(set(A.items()))
print(type(set(A.items())))
# C=set(A).intersection(set(B))
# print(C)
# D= set(A.values()).union(set(B.values()))
# print(D)