# Adding key into dictionay 
# sample Dictionary :{0:10,1:20}
# expected Result :{0:10,1,20,2:30}
Dict = {0:10,1:20}
print(Dict)
Dict[2] = 30
print(Dict)
# another way using built-in function
Dict.setdefault(3,40)
print(Dict)
# another way using built-in function
Dict.update({4:50})
print(Dict)