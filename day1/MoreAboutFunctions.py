#Default Argument Values
#can give default argument values for functions.
def defaultArguments(name, age=18, gender='Not Applicable',somethingelse=None):
    print("name",name)
    print("age",age)
    print("gender",gender)
    print("somethingelse", somethingelse)
defaultArguments("Peanut",20,"Male","Nothing!")
defaultArguments("Peanut",gender="Female")
defaultArguments(name="FailedPeanut",somethingelse="Lot of things to say!")

print("#########################################################")
#Another way:
# just to divide between default and non default parameters
#the parameters before '/' dont have default values
#The parameter after '/' has default values
#the function must be called atleast with 2 arguments else it will give error.
def defaultArgumentsWithPosition(name, age, /,gender='Not Applicable',somethingelse=None):
    print("name", name)
    print("age", age)
    print("gender", gender)
    print("somethingelse", somethingelse)

defaultArgumentsWithPosition("Tommy",20)
defaultArgumentsWithPosition("Jerry",80)
defaultArgumentsWithPosition("Tommy",50,gender="Male")
defaultArgumentsWithPosition("Tommy",90)
