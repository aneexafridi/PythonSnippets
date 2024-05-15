# =========Cursor Method
# cursor() This method is used to create cursor Class object
# we need cursor object so we can call execute() Method.
# Syntax:-
# 	cursor_object = connection_object.cursor()

# 	Arguments may be passed to the cursor() method to control
# 	what type of cursor to create:


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