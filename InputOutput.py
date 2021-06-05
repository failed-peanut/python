#input() is used to get input from console.
#it will be basically read as String.
#The read input is saved in user_name variable below
user_name = input("Please enter your name ")
#converting entered input to upper case using upper() method of string
#getting length of input String with len() method.
print("Your name in all capitals is",user_name.upper(),"and has length", len(user_name))


user_radius = input("Please enter the radius of the circle ")
radius = float(user_radius) #converting input to float data type.
diameter = 2 * radius
print(diameter)
'''
In the above example if you provide String will get below error:
radius = float(user_radius)
ValueError: could not convert string to float: 'a'
'''

print("FailedPeanut")
print("Failed","Peanut") #O/P:Failed Peanut
print("Failed","Peanut", sep="***") #O/P:Failed***Peanut
print("Failed","Peanut", end="***")#O/P:Failed Peanut***
#\n prints the new line
print("\nFailed", end="***")#O/P:Failed***

name=input("\nEnter the name:")
age=input("Enter the age:")
converted_age=int(age) #Convert age to int
print("%s is %d years old." % (name, converted_age))
print(f"Printing with new String Formatting: {name} is {age} years old")


price = 24
item = "banana"
print("The %s costs %d cents"%(item,price)) #O/P:The banana costs 24 cents
print("The %+10s costs %5.2f cents"%(item,price)) #O/P: The     banana costs 24.00 cents
print("The %+10s costs %10.2f cents"%(item,price)) #O/P:The     banana costs      24.00 cents
item_dict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%item_dict) #O/P:The banana costs    24.0 cents