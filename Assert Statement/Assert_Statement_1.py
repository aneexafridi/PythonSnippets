# #-----------------------Assert Statement
# The assert Statement is useful to ensure that a given condition is True.
# If it is not true, it raise AssertionError.
# Syntax:-
# 		assert condition, error_message

# >> If the condition is False then the exception by the name AsserationError
# is raisd along with the message.
# >> If message is not given and the condition is False then also
# AsserationError is raisd without message.

part_1 = 'Equal'
part_2 = 'equal'

assert  part_1 == part_2, 'not Equal'

# for below code run then comment the above code

# for u in range(1,5):
# 	print(u,end=' ')
# 	assert u==3,'message four number'
