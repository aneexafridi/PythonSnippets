# # my solution 

# def divisors(integer):
#  this comprehension return only divisor if not then empty
#     result = [u for u in range(2,integer) if integer % u == 0]
#     counter = 0
#     for v in range(1,integer+1):
#         if integer % v == 0:
#             counter += 1
#     if counter == 2:
#         return f"{integer} is prime"
#     else:
#         return  result
        
# print(divisors(12))


# codewar solution

# def divisors(integer):
#     result = [u for u in range(2,integer) if integer % u == 0]
#     return result or f'{integer} is prime'
        
# print(divisors(11))

def divisors(integer):
	result = [u for u in range(2,integer) if integer % u == 0]
	if len(result) == 0:
		return f'{integer} is prime'
	return result

print(divisors(12))	