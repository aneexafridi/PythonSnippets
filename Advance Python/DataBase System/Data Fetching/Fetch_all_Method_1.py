# ------------------ fetchall method
# fetchall() This method fetch all (or all remaining) rows of a query result set
# and returns a list of tuples.If no more rows are available,it returns an empty list.
# you must fetch all row for the current query before executing new statements
# using the same connection.

# syntax:--
#          rows = cursor_object.fetchall()

from mysql.connector import connect
try:
	connect_object = connect(user='root',
				password='',
				database='world',
				host='localhost',
				port=3306)
	if connect_object.is_connected():
		print('connected')
except:
	print('unable to connect')

mycursor = connect_object.cursor() # created cursor object
sql = 'select name,continent,Region from country'
mycursor.execute(sql) # here execute the query

rows = mycursor.fetchall() 
# we know that fetchone method return list of tuples that's why we use slicing
for u in rows:
	print(u)

mycursor.close()
connect_object.close()