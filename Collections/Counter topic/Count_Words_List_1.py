from collections import Counter

Color_List = ['Red','Blue','Yellow','White','Red','Yellow']
print(Color_List)
Counter_object = Counter() # Empty Counter
for color in Color_List:
	Counter_object[color] +=1
print(Counter_object)

# _________________________equalent the above code___________________

# List = ['Red','Blue','Yellow','White','Red','Yellow']
# Counter_object = Counter(List)

# for key,value in Counter_object.items():
# 	print(key,'=',value)
