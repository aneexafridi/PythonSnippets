#--------------------Creating  table



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

# sql = """
# 		create table Book if not exists
# 		(
# 		id mediumint not null auto_increment primary key,
# 		name varchar(30),
# 		book_Name  varchar(30)
# 		) 
# 		"""
mycursor = connect_object.cursor()

mycursor.execute('show tables')

Table_list = list(mycursor)
print(Table_list)




mycursor.close()
connect_object.close()