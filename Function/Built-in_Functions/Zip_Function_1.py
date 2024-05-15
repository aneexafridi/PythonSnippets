# -------------------zip(*iterables) method
# Make an iterator that aggregates elements from each of the iterables.

# Returns an iterator of tuples, where the i-th tuple contains 
# the i-th element from each of the argument sequences or iterables.
# The iterator stops when the shortest input iterable is exhausted.
# With a single iterable argument, it returns an iterator of 1-tuples.
# With no arguments, it returns an empty iterator. Equivalent to:

# help(zip)

List = ["A","B","C","D"]
Tuple  = ("a","b","c","d")
print(List)
print(Tuple)

print(f'{"List":5}= {"Tuple"}')
for L,T in zip(List,Tuple):
	print(f'{L:5}{"=":4}{T}')

print("\nzip returns Tuple")
for Items in zip(List,Tuple):
	print(Items)