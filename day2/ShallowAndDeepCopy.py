#Shallow and Deep Copy
x=3
y=x
#using id() to get memory location.
#The values may differ based on user Computer.
print(id(x) ,id(y)) #O/P: 1669986256 1669986256
y=3
print(id(x) ,id(y)) #O/P: 1669986256 1669986256
y=30
print(id(x) ,id(y)) #O/P: 1669986256 1669986688
print(x,y) #O/P:3 30

list1=[1,2,3]
list2=[1,2,3]
print(id(list1),id(list2))#O/P:20736488 20736552
list2=list1
print(id(list1),id(list2))#O/P:12413416 12413416
list1[1]=100;
print(list1)#O/P:[1, 100, 3]
print(id(list1),id(list2))#O/P:51145192 51145192
print(list2)#O/P:[1, 100, 3]

###################################
#Copy with the Slice Operator
list1 = ['a','b','c','d']
list2 = list1[:]
print(id(list1),id(list2))#O/P:45443624 45443688
list2[1] = 'x'
print(list1)#O/P:['a', 'b', 'c', 'd']
print(list2)#O/P:['a', 'x', 'c', 'd']
print(id(list1),id(list2))#O/P:45443624 45443688

lst1 = ['a','b',['ab','ba']]
lst2 = lst1[:]
lst2[0] = 'c'
print(lst1) #O/P:['a', 'b', ['ab', 'ba']]
print(lst2) #O/P:['c', 'b', ['ab', 'ba']]

lst2[2][1]="Z" #only reference of sublist is copied not the complete sublist
print(lst1) #O/P:['a', 'b', ['ab', 'Z']]
print(lst2) #O/P:['c', 'b', ['ab', 'Z']]

###################################
#Using the Method deepcopy from the Module copy
#this is how we import other modules in python
# as a java person I see this as similar to import statement in java
from copy import deepcopy
lst1 = ['a','b',['ab','ba']]
lst2 = deepcopy(lst1)
print(lst1) #O/P:['a', 'b', ['ab', 'ba']]
print(lst2) #O/P:['a', 'b', ['ab', 'ba']]
print(id(lst1),id(lst2)) #O/P:31940520 23423624
print(id(lst1[2]),id(lst2[2])) #O/P:23423784 31940328

lst2[2][0]="XYZ"
print(lst2)#O/P:['a', 'b', ['XYZ', 'ba']]
print(lst1)#O/P:['a', 'b', ['ab', 'ba']]
print(id(lst1[2]),id(lst2[2])) #O/P:46689064 48070440



