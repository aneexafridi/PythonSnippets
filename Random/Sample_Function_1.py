# sample() method
# random.sample(population, k)
# Return a k length list of unique elements
# chosen from the population sequence or set.
# Used for random sampling without replacement
#Returns a new list containing elements from
#the population while leaving the original
#population unchanged.

from random import sample
# help(sample)
print("List of All Cards\n")
cards = list(range(1,53))
print(cards)

print('\n')
print(sample(cards,k=4))
# randomly  selected  4 cards from List of cards
