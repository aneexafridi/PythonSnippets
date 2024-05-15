from numpy import empty

Length = int(input("Enter Length: "))

# shape word no need to write in formal argument of function
# simple for readability
Empty = empty(shape=Length,dtype="U10") 
print(Empty)

for u in range(Length):
	Empty[u]=input("Enter Your Name: ")
for v in Empty:
	print(v)


# using string  the best way to use char.array
