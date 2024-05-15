# ------------Execute Method
# execute() this method is used to execute given SQL queries.
# we need cursor object so we can all execute() method.
# Syntax:-
# 		cursor_object.execute(sql,param=None,multi=False)

# Sql - It is sql qurey,
# param - The parameter found in the tuple or dictionary param
# are bound to the variables in the operation.
# Multi - execute() returns an iterator if multi is True.

# eg:-

# mycursor = connect_object.cursor()
# mycursor.execute('select * from table_Name')
# or 
# sql = 'select * from table_Name'
# mycursor.execute(sql)

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