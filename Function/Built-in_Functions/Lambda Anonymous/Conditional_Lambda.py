
# def Greater(value):
# 	return value if value > -1 else 'negative'
# equivalent  to anonymous function


Greater = lambda value: value if value > -1 else 'negative'

print(Greater(-9))
