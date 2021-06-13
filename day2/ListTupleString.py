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
OR
__len__()
'''
print(myString.__len__())#Output:18
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
print("----------Reversing elements Starts----------")
print(myList[::-1])#Output:[False, 1.0, 3, 2, 1, 'List_how I learnt Python', 'List_failedPeanut']
print(myTuple[::-1])#Output:(True, 2.0, 30, 20, 10, 'Tuple_how I learnt Python', 'Tuple_failedPeanut')
print(myString[::-1])#Output: gnirtS fo elpmaxE
'''
[begin_index:end_index:step] - by leaving begin_index and end_index off and specifying a step of -1, it reverses.
'''
print(myList[0:6:2])#Output: ['List_failedPeanut', 1, 3]
'''
Our List:             ["List_failedPeanut","List_how I learnt Python",1,2,3,1.0,False]
specifying each index:           0        ,            1             ,2,3,4, 5 ,   6 
[0:6:2] : This will start at index 0 (0 included), end at index 6 (6 excluded),skipping every 2nd element
'''
print(myList[-1:0:-2])#Output: [False, 3, 1]
#begin_index=-1,end_index=0,step=-2
print("----------Reversing elements Ends----------")
###########################################################
#sublists
#Lists can have sublists as elements.
# These sublists may contain sublists as well, i.e. lists can be recursively constructed by sublist structures.
person = [["Jack","Sparrow"],["17, Oxford Str", "12345","London"],"07876-7876"]
name = person[0]
print(name) #prints 1st sublist O/P: ['Jack', 'Sparrow']
print(person[2]) #07876-7876
#print(person[3]) # IndexError: list index out of range

sometuple=(["Tuple","Sparrow"],["18, Oxford Str", "12345","India"],"07876-780076")
print(sometuple[1])#OutPut:['18, Oxford Str', '12345', 'India']
#sometuple[1]="Replace with This Data"
#print(sometuple)#TypeError: 'tuple' object does not support item assignment

someString="My String"
substring=someString[0:2]
print(someString)#Output:My String
print(substring)#Output:My
###########################################################
#Slicing
str = "Python is Scripting Language"
first_six=str[0:6]
print(first_six) # gets first six characters O/P: Python
print(str[:6]) # gets first six characters O/P: Python
print(str[5:]) # gets next characters starting from index 5 O/P: n is Scripting Language
print(str[:])#prints whole String O/P: Python is Scripting Language
print(str[5:-5]) #starting from 5th character and ignoring 5 characters from last O/P: n is Scripting Lan
print(str[0:-10])#Exclude last 10 characters O/P: Python is Scriptin
print(str[0:100])#prints whole String without error O/P: Python is Scripting Language
print(str[0:1])#prints first character O/P:P
print(str[-100:])#prints whole string O/P: Python is Scripting Language

cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
print(cities[1:4])# O/P: ['London', 'Paris', 'Berlin']
print(cities[0:-4])#O/P: ['Vienna', 'London']
print(cities[100:200])#O/P:[]
#Lists are similar to Strings in Slice operation.

#Slicing works with three arguments as well.
# If the third argument is for example 3, only every third element of the list, string or tuple from the range of the first two arguments will be taken.
str = "Python under Linux is great"
print(str[::3]) #prints every 3rd character in String O/P:Ph d n  e
print(str[::-2])#ignores all 2nd character from backwards and prints O/P: tegs ui en otP
print(str[::-1])#prints whole string reverse (character by character) O/P: taerg si xuniL rednu nohtyP

print(cities[::2])#even number cities ignored O/P:['Vienna', 'Paris', 'Zurich']
print(cities[::-2])#O/P:['Hamburg', 'Berlin', 'London']
print(cities[::200])#Prints only 1st city O/P: ['Vienna']
print(cities[::-200])#Prints only last city O/P: ['Hamburg']

###################################
#Concatenation of Sequences
firstname="Tom"
lastname="jerry"
print(firstname+" "+lastname) #O/P:Tom jerry

colours1=["red","blue"]
colours2=["orange"]
finalColours=colours1+colours2
print(finalColours) #O/P: ['red', 'blue', 'orange']
colours1+=colours2
print(colours1) #O/P:['red', 'blue', 'orange']

#tuples are Immutable
#existing tuple cant be modified but it can result in new tuple.
tuple1=("tuple",1)
tuple2=("tuple",2)
newTuple=tuple1+tuple2
print(newTuple)#Output:('tuple', 1, 'tuple', 2)
###################################
#Checking if an Element is Contained
characters=['a','b','c',"x","y"]
string="Hello Peanut"
mytuple=("my","tuple")
print('z' in characters) #O/P: False

print('e' in string) #O/P: True

print('tuple' not in mytuple)#O/P: False
###################################
###########################################################
#Repetitions (*)
repeatList=["jan","feb","march"]
print(2*repeatList) #O/P:['jan', 'feb', 'march', 'jan', 'feb', 'march']
print(3*"Hello"+"-") # O/P: HelloHelloHello-
print("Hi-"*4) #O/P:Hi-Hi-Hi-Hi-
print(4*4) #O/P: 16

testList=["a","b","c"]
multipleList=[testList]*2
print(multipleList) #O/P:[['a', 'b', 'c'], ['a', 'b', 'c']]

multipleList[0][0]="z"
print(multipleList) #O/P:[['z', 'b', 'c'], ['z', 'b', 'c']]

myTuple=("my","tuple",10)
resultTuple=myTuple*3
print(resultTuple)#Output:('my', 'tuple', 10, 'my', 'tuple', 10, 'my', 'tuple', 10)
###########################################################
##################################
#pop and append
fruitList=["apple","orange"]
returnValueOfappend=fruitList.append("banana")
print(fruitList) #O/P:['apple', 'orange', 'banana']
print(returnValueOfappend) #O/P:None

popFruit=fruitList.pop();
print(popFruit)#O/P:banana
print(fruitList) #O/P: ['apple', 'orange']

#'str' object has no attribute 'append'
#you cant append a tuple- Immutable!
#myTuple=(1,2,3)
#print(myTuple.pop())#'tuple' object has no attribute 'pop'
###################################

#extend
listNumbers1=[1,2,3,4,5,6]
listNumbers2=[7,8,9]
listNumbers1.extend(listNumbers2)
print(listNumbers1) #O/P:[1, 2, 3, 4, 5, 6, 7, 8, 9]
listNumbers1.extend([0,0,0])
print(listNumbers1)#O/P:[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0]

someString="Hello"
listNumbers2.extend(someString)
print(listNumbers2) #O/P: [7, 8, 9, 'H', 'e', 'l', 'l', 'o']

listDigi=[1,3,5,6,8]
tupleAlpha=('a','b','bo')
listDigi.extend(tupleAlpha)
print(listDigi)#O/P: [1, 3, 5, 6, 8, 'a', 'b', 'bo']
######################################################################

###################################
#Extending and Appending Lists with the '+' Operator
level = ["beginner", "intermediate", "advanced"]
other_words = ["novice", "expert"]
print(level + other_words)#O/P:['beginner', 'intermediate', 'advanced', 'novice', 'expert']
level+=["super expert"]
print(level)#O/P:['beginner', 'intermediate', 'advanced', 'super expert']

string1="Hello"
string2="Peanut"
print(string1+string2)#Output:HelloPeanut
###################################
'''
NOTE:
#the "+" operator is  slower than the append method.
'''
###################################
#Removing an element with remove()

colours = ["red", "green", "blue", "green", "yellow"]
removedColor=colours.remove("yellow")#it returns nothing. void/None
print(removedColor) #O/P:None
print(colours)#O/P:['red', 'green', 'blue', 'green']
#colours.remove("yellow") #O/P:  colours.remove("yellow") ValueError: list.remove(x): x not in list

colours.remove("green") #removes the first occurance of green
print(colours) #O/P:['red', 'blue', 'green']

###################################
######################################################################
#Find the Position of an Element
colours = ["red", "green", "blue", "green", "yellow"]
print(colours.index("green")) #O/P:1
print(colours.index("green",2))#O/P:3
print(colours.index("green",3,4))#O/P:3
#print(colours.index("green",4,8))#O/P:print(colours.index("green",4,8))#O/P:3 ValueError: 'green' is not in list
print(colours.index("green",0,len(colours)))#O/P:1

string="Hello Failed Peanut"
print(string.index('F'))#Output:6

tuple=("1",2,"3")
print(tuple.index(2))#Output:1

######################################################################
###################################
#insert
lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
print(lst)#O/P:['German is spoken', 'in Germany,', 'Austria', 'and', 'Switzerland']
lst.insert(100,"hello")
print(lst) #O/P:['German is spoken', 'in Germany,', 'Austria', 'and', 'Switzerland', 'hello']

#cant use insert method with string and tuple
###################################
