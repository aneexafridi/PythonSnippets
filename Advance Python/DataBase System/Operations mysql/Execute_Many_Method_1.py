# ---------------Execute many method
# executemany() this method is used to prepare given SQL query and
# executes it against all parameter sequeneces or mappings founds in the 
# swquenece seq_of_params.
# with the executemany() method, it isnot possible to specify multiple
# statements to execute in the sql argument.

# Syntax:-
# 		cursor_object.executemany(sql,seq_of_params)


from mysql.connector import connect

try:
	connect_object = connect(
		user='root',
		password='aqsaaqsa',
		host='localhost',
		database='python_db')
	if connect_object.is_connected():
		print('success connection')
except:
	print('unable to connect')
else:
	cursor_object = connect_object.cursor()

	sql = 'insert into bookstore(Author,bookname) values(%s,%s)'
	params = [('Don megiz','four argument'),('Toa ta ching','lao tzu')]

	cursor_object.executemany(sql,params)
	connect_object.commit()
finally:
	cursor_object.close()
	connect_object.close()
