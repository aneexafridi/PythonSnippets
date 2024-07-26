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
"""
Note: If there is more than one element with the same value, the index of the first instance of the value will be returned:
"""

#get the values 10 and 20 only
print(numbers[:2])  #first to second position

#change the first element
#change it from having a value of 1 to having a value of 40
numbers[0] = 40

#add the integer 40 to the end of numbers
numbers.append(40)

# add more than one item
#add the integers 40,50,60 to the end of numbers
#The numbers need to be enclosed in square brackets

numbers.extend([40,50,60])

"""
And what if you don't want to add an item to the end of an array? Use the insert() method, to add an item at a specific position.

The insert() function takes two arguments: the index number of the position the new element will be inserted, and the value of the new element.
"""
numbers.insert(0,90)