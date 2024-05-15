from pandas import  DataFrame,read_csv

Read_data = read_csv('file_name_with_the_extention.txt',sep='\n')
print(Read_data)
DF = DataFrame(data=Read_data)
DF.to_csv('give_the_Name_to_the_file_with_extention.csv')