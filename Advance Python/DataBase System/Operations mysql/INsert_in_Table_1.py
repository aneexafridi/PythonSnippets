#--------------------Insert   data in table



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

mycursor = connect_object.cursor() # created cursor object
sql = 'insert into Book(Author,book_Name) Values("Echkart","Stillness")'
mycursor.execute(sql) # here execute the query
connect_object.commit()
# mycursor.execute('select * from book')
# Table_list = list(mycursor)
# print(Table_list)

mycursor.close()
connect_object.close()