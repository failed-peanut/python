#Control Flow Tools : if, elif, else, for, range(), break, continue, while, pass

#using if.. elif, else
def functionToTestIf(age):
    if(age<18):
        print("You are not adult!")
    elif(age>18 and age<100):
        print("You are Adult!")
    else:
        print("You are Dead!")

functionToTestIf(10)
functionToTestIf(20)
functionToTestIf(100)

#using for .. range()
def functionToTestFor(number):
    for i in range(number):
        print("Number is",i)
functionToTestFor(10)#it prints from 0 to 9

#using break.. continue
#using pass
#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.
def functionToTestBreakContinue(number):
    for i in range(number):
        if(i%2==0):
            continue
        if (i == 11):
            pass
        if(i%2>0):
            print("Odd Number is", i)
        if(i==13):
            break

functionToTestBreakContinue(20)

#using while
def functionToTestWhile():
    i=10
    j=0
    while(j<i):
        print(j)
        j=j+1
functionToTestWhile()#prints 0 to 9

