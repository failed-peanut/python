#Two ways to iterate elements in List
a= ["item1","item2","item3"]
for elem in a:#first method use normal for loop
    print(elem)
'''
O/P:
item1
item2
item3
'''


#to understand the 2nd way- need to know what range function does
for i in range(len(a)):
    print("Data from list={} with index {}".format(a[i],i))

'''
O/P:Data from list=item1 with index 0
Data from list=item2 with index 1
Data from list=item3 with index 2
'''