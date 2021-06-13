#list - Lists are used to store multiple items in a single variable.
'''
Lists are ordered.
Lists can contain any arbitrary objects.
List elements can be accessed by index.
Lists can be nested to arbitrary depth.
Lists are mutable.
Lists are dynamic.
'''
#tuple - tuple are used to store multiple items in a single variable.
'''
Tuples are identical to lists in all respects, except for the following properties:
Tuples are defined by enclosing the elements in parentheses (()) instead of square brackets ([]).
Tuples are immutable.
'''
#strings - internally list of characters.
'''
In Python, Strings are arrays of bytes representing Unicode characters. 
However, Python does not have a character data type, a single character is simply a string with a length of 1. 
Square brackets can be used to access elements of the string
'''
###########################################################
print("----------Access Items Starts----------")
myList =["List_failedPeanut","List_how I learnt Python",1,2,3,1.0,False]
myTuple=("Tuple_failedPeanut","Tuple_how I learnt Python",10,20,30,2.0,True)
myString="Example of Strings"
print(myList[1])#Output: List_how I learnt Python
print(myTuple[1])#Output: Tuple_how I learnt Python
print(myString[1])#Output: x
'''
NOTE: Everything starts at index 0
'''
print("-----Access Last Item-----")
print(myList[-1])#Output: False
print(myTuple[-1])#Output: True
print(myString[-1])#Output: s
'''
NOTE:
when last element can be accessed with -1 the second last can be accessed with -2 and so on.
so, what I learnt is, it starts with 0 and ends with its length-1
reversing it: it starts with -1 and ends with -(length)
if list OR tuple or String is of length 7 then it's range will be between.
-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6
'''
print(myTuple[-7])#Output: Tuple_failedPeanut
#print(myString[-200])# This will cause error- IndexError: string index out of range
print("----------Access Items Ends----------")
###########################################################
print("----------Iterate elements Starts----------")
'''
Length of any of the above Data Structure/Data type (list, tuple, string) can be retrieved with inbuilt function called len()
len(myString) is 7
'''
#using simple for loop
for i in myString:#in is the keyword to check in some iterable/list/tuple/string
    print(i)#This will print all the characters in myString one after another on each line along with space (if string has any space in it)

#using range()
for i in range(len(myTuple)):
    print(myTuple[i])#when we use range() it itereate through indexes so need to specify index that we need to access/print

#just printing
print(myList)#Output:['List_failedPeanut', 'List_how I learnt Python', 1, 2, 3, 1.0, False]
print(myTuple)#Output:('Tuple_failedPeanut', 'Tuple_how I learnt Python', 10, 20, 30, 2.0, True)
print(myString)#Output:Example of Strings
print("----------Iterate elements Ends----------")
###########################################################


