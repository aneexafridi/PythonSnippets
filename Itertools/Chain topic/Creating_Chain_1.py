from itertools import chain
# help(chain)

# chain is a class in module itertools
# Make an iterator that returns elements from the first iterable
# until it is exhausted, then proceeds to the next iterable,
# until all of the iterables are exhausted. Used for treating
# consecutive sequences as a single sequence. Roughly equivalent to:
# ('ABC','DEF') -> ABCDEF

iterable = ('ABC','DEF')

Chainning = chain(*iterable)

print(''.join(Chainning))