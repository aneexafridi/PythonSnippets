# -----------------Creating Connection
# connect() - This method is used to open or establish a new 
# connection. It returns an object representing the connection.

# Syntax:-
# 		connection_object = connect(
# 				user='username',
# 				password = 'password',
# 				host='localhost',
# 				port=3306)

from mysql.connector import connect
# help(connect)
Connect_object = connect(
	user='root',
	password='aqsaaqsa',
	host='localhost',
	port=3307
	)

if Connect_object.is_connected():
	print('Connected')
else:
	print('Not Connected')

# second way to create a connection

# config = {
# 		'user':'root',
# 		'password':'aqsaaqsa',
# 		'host':'localhost',
# 		'port':3307
# 		}

# Conncet_object = connect(**config)