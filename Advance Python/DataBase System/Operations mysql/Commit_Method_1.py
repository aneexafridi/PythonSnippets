# ------------------------commit method
# this method is used to save inserted row in the table.
# it is required to make the changes,otherwise no changes are made
# to the table.
# This method sends a COMMIT statement to the MySQL server committing
# the current transaction.Since by default connector/python does not
# autocommit, it is important to call this method after every transaction
# that modifies data for tables that use transactional storage engines.


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
sql = 'insert into Book(Author,book_Name) Values("La Zue","Doa change")'
mycursor.execute(sql) # here execute the query
connect_object.commit()
mycursor.execute('select * from book')
Table_list = list(mycursor)
print(Table_list)

mycursor.close()
connect_object.close()