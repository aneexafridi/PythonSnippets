# ------------close Cursor Method
# close() this is used to close the cursor, resets all results,
# and ensures that the cursor object has no reference to its original
# connection object.

# Syntax:--
# 		cursor_object.close()

from mysql.connector import connect

try:
	Connect_object = connect(
		user='root',
		password='aqsaaqsa',
		host='localhost',
		port=3306
		)
	if Connect_object.is_connected():
		print('Connected')
except:
	print('Unable to connect')

mycursor = Connect_object.cursor()

mycursor.execute('show databases',multi=False)

for u in mycursor:
	print(u)

Connect_object.close()
mycursor.close()