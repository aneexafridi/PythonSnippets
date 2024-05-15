#-------------------rowcount Property
# This read-only property returns the number of rows returned for select
# statements, or the number of rows affected by DML statements such AS 
# # Insert or update

# Syntax:-
# 		cursor_object.rowcount

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
mycursor.execute('select * from book')
Table_list = list(mycursor)
print('\n')
print(Table_list)
print("Total Rows in book table",end=': ')
print(mycursor.rowcount)


mycursor.close()
connect_object.close()