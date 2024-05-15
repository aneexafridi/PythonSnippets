a = 10
b = 5
try:
# for NameError using other values instead of a and b e.g (g,name_some,f,k,something)
	d = a/b 
except (NameError,ZeroDivisionError) as except_error:
	print(except_error)
else:
	print(d)
finally:
	print('Finally statement')