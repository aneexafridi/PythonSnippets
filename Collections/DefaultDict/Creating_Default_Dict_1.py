from collections import defaultdict

Character = [('a',1),('b',2),('a',3),('c',4),('b',5)]
print(Character)
print()
d = defaultdict(list) # default value pass "list"
for k, v in Character:
    d.setdefault(k,[]).append(v) # below same work line no 9
    # d[k].append(v)

# setdefault method return list  so then we can perform operations
# as on list type

print(sorted(d.items()))