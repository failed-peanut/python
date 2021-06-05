
def function1():
    print("Inside Function1")#O/P:Inside Function1
    print("Second line of Function1")#O/P: Second line of Function1

print("Outside Function1") # this will executed first O/p: Outside Function1

#x is given as parameter.
def function2(x):
    return 2*x

#there are 2 parameters in this function.
def function3(x,y):
    return x+y


'''There can be a situation where you don't know how many keyword arguments will be passed into the function. 
In such a scenario we can use Kwargs.

To use kwargs we put ** in front of the argument.


Remember: When you attach a ** in front, you will be receiving a dictionary of arguments.'''
def functionkwargs(**names):
    print(names)#O/P:{'name1': 'sam', 'name2': 'Tom', 'name3': 'jam', 'name4': 1, 'name5': 2, 'name6': 3}


#calling function
function1()
a=function2("4")
x=function2(4)
print(a,x) #O/P:44 8
sum=function3(5,5) #O/P: 10
print(sum)
# calling function2() without argumnet will cause below error:
'''TypeError: function2() missing 1 required positional argument: 'x' '''

functionkwargs(name1="sam",name2="Tom",name3="jam",name4=1,name5=2,name6=3)



