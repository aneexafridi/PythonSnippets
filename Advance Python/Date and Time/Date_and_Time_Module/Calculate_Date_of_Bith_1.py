from datetime import date

y = 1992
m = 5
d = 14
Date_Of_birth = date(y,m,d)
print(Date_Of_birth)
Date = date.today()
print(Date)
Age = Date.year-Date_Of_birth.year-((Date.month,Date.day)<(Date_Of_birth.month, Date_Of_birth.day))
print("Age: ",Age)

# Same the above code ((date.mont,date.day)<(......,....))
# ((Date.month,Date.day)<(Date_Of_birt.month,Date_Of_birth.day))  == True or False
print("\n\n")
print(5-False) # False = 0
print(5-True)  # True  = 0
print(False-True) # 0 - 1 = -1
print(True-False) # 1 - 0 = 1
