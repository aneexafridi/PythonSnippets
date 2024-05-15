# from pandas import DataFrame,read_csv,Series
# from numpy import nan

List = ['a','c','b']
print(sorted(List,key=lambda value: enumerate(List)))
print(List)






# # t =read_csv("business_salary.csv")
# # print(t.info())


# # # Person = {
# # # 		"first_Name":['Ali','Fawad','Shahab'],
# # # 		"last_Name":['Zaman','Afridi','Afridi'],
# # # 		"marks":[11,44,55],
# # # 		"Email":['alizaman@gmail.com','fawadafridi@gmail.com','shahabafridi@gmail.com']
# # # 		}
# # # DF = DataFrame(data=Person)
# # # print(DF)
# # # print('\n')
# # # print(DF.index) # .index is attribute of DataFrame
# # # print(DF.columns) # .columns is attribute of DataFrame
# # # print('\n')



# df = DataFrame(
#     {
#         "col1": ["a", "a", "b", "b", "a"],
#         "col2": [1.0, 2.0, 3.0, nan, 5.0],
#         "col3": [1.0, 2.0, 3.0, 4.0, 5.0]
#     },
# )
# # print(df)
# df2=df.copy()

# df.loc[0,'col1'] =  'Z'
# df2.loc[4,'col3'] = 99
# print(df)
# print('\n\n',df2)

# print('\n',df.compare(df2))
