from operator import *

# Operation            Syntax        		Function
# Addition			 a + b        		add(a, b)
# Concatenation        seq1 + seq2		concat(seq1, seq2)
# Containment Test     obj in seq          contains(seq, obj)
# Division			 a / b               truediv(a, b)
# Division			 a // b              floordiv(a, b)
# Bitwise and 		 a & b               and_(a, b)
# Bitwise Inversion		~ 				ainvert(a)
# Bitwise Or           a | b               or_(a, b)
# Exponentiation       a ** b              pow(a, b)
# Identity             a is b              is_(a, b)
# Identity             a is not b          is_not(a, b)
# Indexed Assignment   obj[k] = v          setitem(obj, k, v)
# Indexed Deletion     del obj[k]          delitem(obj, k)
# Indexing             obj[k]				 getitem(obj, k)
# Left Shift           a << b              lshift(a, b)
# Modulo                a % b               mod(a, b)
# Multiplication		    a * b               mul(a, b)
# Negation (Arithmetic)     - a               neg(a)
# Negation (Logical)	      not 				anot_(a)
# Positive				 + 				apos(a)
# Right Shift			    a >> b              rshift(a, b)
# String Formatting       s % obj         mod(s, obj) 
# Subtraction              a - b 			sub(a, b)
# Truth Test               obj              truth(obj)
# Ordering                a < b              lt(a, b)
# Ordering                a <= b             le(a, b)
# Equality                a == b            eq(a, b)
# Difference              a != b             ne(a, b)
# Ordering                a >= b               ge(a, b)
# Ordering                a > b 				gt(a, b)
# Slice Assignment   seq[i:j]=values  setitem(seq, slice(i, j), values)
# Bitwise Exclusive Or a ^ b              xor(a, b)
# Slice Deletion		del seq[i:j]     delitem(seq, slice(i, j))
# Slicing				seq[i:j]         getitem(seq, slice(i, j))

# Matrix Multiplication    a @ b             matmul(a, b) use matrix type

print(and_(True,False))  # equivalent = True and False
print(or_(True,False))   # equivalent = True  or False

print()
seq = []
seq[0:3] = (1,2,3)
print(seq)