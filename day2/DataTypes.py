#string, int, float
#we can use 'type()' inbuilt function to check what is the data type of the variable.
somestring="This is some String"
intvalue=20
floatvalue=20.3

print("type is:",type(somestring),"somestring value:",somestring)#type is: <class 'str'>
print("type is:",type(intvalue),"intvalue value:",intvalue)#type is: <class 'int'>
print("type is:",type(floatvalue),"floatvalue value:",floatvalue)#type is: <class 'float'>


#its not mandatory to declare what data type is it.
#we can reassign the data to other data type.
floatvalue="see this is String Now"
print("type is:",type(floatvalue),"floatvalue value:",floatvalue)#type is: <class 'str'>