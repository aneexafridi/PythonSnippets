from collections import Counter

# help(Counter.most_common)

words = [
 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
]

Counter_obj = Counter(words)
print(Counter_obj)

print()
print(Counter_obj.most_common(1))