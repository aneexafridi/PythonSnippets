#		 fetch data from table

from mysql.connector import connect

try:
	connect_object = connect(
		user='root',
		password='aqsaaqsa',
		host='localhost',
		database='python_db')
	if connect_object.is_connected():
		print('Success to Connect')
except:
	print('Unable to connect')
else:
	cursor_object = connect_object.cursor(prepared=True)
	sql = 'select * from student'
	cursor_object.execute(sql)
	rows = cursor_object.fetchall()
	print(list(rows))
	print('\nTotal rows: ',cursor_object.rowcount)
finally:
	cursor_object.close()
	connect_object.close()
