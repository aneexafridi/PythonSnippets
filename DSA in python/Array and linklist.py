from array import array

"""
The general syntax for creating an array looks like this:

variable_name = array(typecode,[elements])
"""

numbers = array("i",[1,2,3,4])
# print(numbers)
for num in numbers:
    print(num)
    
print(numbers[0]) # gets the 1st element
print(numbers[-1]) #gets last item
print(numbers[-2]) #gets second to last item

#search for the index of the value 10
print(numbers.index(10))