from mysql.connector import connect
try:
	connect_object = connect(
		user='root',
		password='aqsaaqsa',
		host='localhost',
		database='python_db')
	if connect_object.is_connected():
		print('Success connection')
except:
	print('Unable to connection')
# else statement execute when try pass (mean) no any problem occur in try block

else:
	Cursor_object = connect_object.cursor()
	
	sql = """
		insert into Student(name,roll)
		values(%(N)s,%(R)s)
		"""
	# param = is parameter which can be dictionary or tuple
	param = {'N':'Jena','R':'73'}
	Cursor_object.execute(sql,param)
	# commit method is commit the update or changes in table
	connect_object.commit()

# finally statement always executed that's why  i put the close statement

finally:
	Cursor_object.close()
	connect_object.close()
