# ------------------Fetchmany method 
# fetchmany() this method fetches the next set of rows of a qurey result
# and returns a list of tuples. If no more rows are available,it returns
# empty list.
# The number of rows returned can be specified using the size argument,
# which defaults to one.Fewer rows are returned if fewer rows are available
# than specified.
# you must fetch all rows for the current qurey before executing new statements
# using the same connection.
# Syntax:-
# 		rows = cursor_object.fetchmany(size=1)
# 		Size by default set 1
#      we can customize the size


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

mycursor = connect_object.cursor(buffered=True) # created cursor object
sql = 'select * from book'
mycursor.execute(sql) # here execute the query

rows = mycursor.fetchmany(size=3) 
# we know that fetchone method return list of tuples that's why we use slicing
for u in rows:
	print(u)

mycursor.close()
connect_object.close()