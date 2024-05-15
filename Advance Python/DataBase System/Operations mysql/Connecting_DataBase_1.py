# ---------connect  method
# connect() This method is used to open or establish a new connection.
# it returns an object representing the connection.
# Syntax:-
# 		connect_object = connect(
# 				user='username',
# 				password='password',
# 				database='database_Name',
# 				host='localhost',
# 				port=3306)

# 
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

mycursor = connect_object.cursor()

mycursor.execute('show tables')

Table_list = list(mycursor)
print(Table_list)
print('\nTotal tables in my_db database')
print(len(Table_list))

mycursor.close()
connect_object.close()


