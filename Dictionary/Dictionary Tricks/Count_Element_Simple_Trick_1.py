# from collections import defaultdict
List = [1,2,3,4,2,21,2,3,4,4]

# Dict = dict()
# for u in List:
# 	Dict[u] =List.count(u)
# print(Dict)
Dict = dict(zip(set(List),map(List.count,set(List))))
print(Dict)
# ---------------------------------------------------------------
# Count_element = tuple(map(List.count,set(List)))
# Dict = {}
# for k, v in zip(set(List),Count_element):
# 	Dict[k] = v
# print(Dict)
# ---------------------------------------------------------------
#  for String
Word = 'mississippi'
print(Word)
print(dict(zip(set(Word),map(Word.count,set(Word)))))
# ---------------------------------------------------------------
# # also can use built-in procedure

from collections import Counter
print(sorted(Counter(List).items()))