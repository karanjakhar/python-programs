#Program to demonstrate the use of various list functions
a=[9,2,3,4,5,2782]
b=[5,4,3,2,1,2782]
print(a[::-2])
print(b)
sum=0
for i in range(0,6):
    sum+=a[i]
print(sum)

mul=1
for i in range(0,6):
    mul*=a[i]
print(mul)
c=a
d=a.copy()
e=a[0:3]
print(c)
print(d)
print(e)

print('list a :',a)
print('list b :',b)
#demostrating the use of index function
print('index of value 5 in list a : ',a.index(5))
#demostrating the use of count function
print('number of times 5 is present in the list a : ',a.count(5))
#demostrating the use of pop function
a.pop(2)
print('a[2] is popped and updated list a is :',a)
#demostrating the use of insert function
a.insert(2,96)
print('96 is inserted at index number 2 and updated list a is : ',a)
#demostrating the use of extend function
a.extend(b)
print('a is extended with list b and updated list a is : ',a)
#demostrating the use of reverse function
a.reverse()
print('reverse of list a is : ',a)
#demostrating the use of sort function
a.sort()
print('sorted list a is : ',a)
#demostrating the use of remove function
b.remove(5)
print('value 5 is removed from the list b and the updated list is : ',b)
#-----------------------------------------------------------------------------
#Program to demonstrate the use of various functions and methods
a=[1,2,3,4,5,2782]
b=[5,4,3,2,1,2782]
#demonstrating the use of max function
print('max :',max(a))
#demonstrating the use of min function
print('min : ',min(a))
#demonstrating the use of len function
print('len :',len(a))
#demonstrating the use of cmp function
#print('cmp: ',cmp(a,b))
#-----------------------------------------------------------------------------
#Program to demonstrate the use of various list operations
a=[1,2,3,4,5,'sandeep']
b=[6,7,8,9,10,'singh']
print('list a : ',a)
print('list b : ',b)
#adding two lists using + operator i.e. concatination
print(a+b)
#replicating list using * operator
print(a*3)
#demonstrating slicing on list
print(a[2])
print(a[0:2])
print(a[2:])
print(a[:2])
#appending list 
a.append(10)
print(a)
#demonstrating how to delete a value
del a[2]
print(a)
#updating list values
a[2]=89
print(a)
