Countries = ['Pakistan','India','UK','Germany','USA']
cities    = ['islamabad','Deli','blorg','Takno','New Yark']


Dict = dict(zip(Countries,cities))
print(Dict)

# dict function take only one parameter 
# which can be **kwargs or mapping like (a=1,b=2)
# and D[k] = value ,or List in tuples [(),()] or
# Tuple in tuples ((),())
# zip function return tuples that's why we pass the list of Tuples
