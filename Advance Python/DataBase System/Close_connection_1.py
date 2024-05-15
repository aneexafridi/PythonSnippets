# -------------------Close Connection
# close() This method is used to close the connection.
# Syntax:-
# 	 connection_object.close()

from mysql.connector import connect

Connect_object = connect(
	user='root',
	password='aqsaaqsa',
	host='localhost',
	port=3307
	)

print(Connect_object.is_connected())
Connect_object.close()
print("After closed the connec_object")
print(Connect_object.is_connected())