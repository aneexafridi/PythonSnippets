# ---------------Fetchone Method
# fetchone() this method retrieves the next row of a query result
# set and returns a single sequence,or None if no more rows are available.
# by default, the returned tuple consists of data
# returned by the MySQL server. converted to Python objects. If the 
# cursor is a raw cursor, no such conversion occurs.
# You must fetch all rows for the current query before
# executing new statements using the same connection.
# syntax:--
#          row = cursor_object.fetchone()


from mysql.connector import connect
try:
	connect_object = connect(user='root',
				password='aqsaaqsa',
				database='my_db',
				host='localhost',
				port=3306)
	if connect_object.is_connected():
		print('connected')
except:
	print('unable to connect')

mycursor = connect_object.cursor() # created cursor object
sql = 'select * from book'
mycursor.execute(sql) # here execute the query

row = mycursor.fetchone() 
# we know that fetchone method return tuple that's why we use slicing

print(f'Id \t\tAuthor: \t\tBook Name')
while row is not None:
	print(f'{row[0]}\t\t{row[1]}\t\t{row[2]}')

	print(row)
	row = mycursor.fetchone()

mycursor.close()
connect_object.close()