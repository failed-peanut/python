

#Examples of Lambda Expressions/Functions
n=[1,2,2,3] #declare a list
#The below lamda Expression which take two arguments
#it returns sum of the two arguments
sum=lambda x,y: x+y

#The below lambda function checks the max number and return accordingly.
max=lambda x,y: x if x>y else y

#The below expression returns the square of the number
#we use ** to calculate square in python or to represent 'power of'
square_lambda=lambda x:x**2
#returns list of squares to a list using square_lambda function
square_list=list(map(square_lambda,n))

#write a function which takes list and returns its squares
def squares_of_list(list_data):
    return list(map(square_lambda,list_data))

#create a filter with lambda functions
#this will check if x is greater than 10
greater_than_10Filter=lambda x: x>10

#creating even number filter
even_number_filter=lambda x:x%2==0

#here we are passing the list and lambda expression name as arguments to a function.
def filter_example(list_data,filter_):
    return list(filter(filter_,list_data))


#functools is a module in python which has reduce method.
#we are importing reduce method
from functools import reduce

#this lambda expression adds up x and y
reduce_data_filter_1=lambda x,y:x+y

#this lambda expression multiplies x and y
reduce_data_filter_2=lambda x,y:x*y

#a function that takes list of values and a lambda expression as input
#the reduce() function will apply the filter defined or passed to the input data
#reduce() function was moved to functools.
def reduce_example(list_data,reduce_filter):
    return reduce(reduce_filter,list_data)

print(f"sum-1: {sum(10,20)}")#O/P:sum-1: 30
print(f"sum-2: {sum(10,y=11)}")#O/P:sum-2: 21


print(f"Max-1: {max(10,y=11)}")#O/P:Max-1: 11
print(f"Max-2: {max(10,101)}")#O/P:Max-2: 101

print(square_list)#O/P:[1, 4, 4, 9]
print(f"squares of List: {squares_of_list([4,3,2,1])}")#O/P:squares of List: [16, 9, 4, 1]

print(f"Filter List-1: {filter_example([4,3,20,1],greater_than_10Filter)}")#O/P:Filter List-1: [20]
print(f"Filter List-2: {filter_example([4,3,20,1],even_number_filter)}")#O/P:Filter List-2: [4, 20]


print([x for x in n if x>2] )#O/P:[3]

print(f"Reduce List-2: {reduce_example([4,3,2,1],reduce_data_filter_1)}")#O/P:Reduce List-2: 10
print(f"Reduce List-2: {reduce_example([4,3,2,1],reduce_data_filter_2)}")#O/P:Reduce List-2: 24






