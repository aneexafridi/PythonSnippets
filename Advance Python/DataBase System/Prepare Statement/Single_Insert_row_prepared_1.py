# 			Single row insert

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
	sql = 'insert into Student(name,roll) value(?,?)'
	param = ('Shahab',38)
	cursor_object.execute(sql,param)
	connect_object.commit()
finally:
	cursor_object.close()
	connect_object.close()


