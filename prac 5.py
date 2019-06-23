print("write the program to demonstrate the use of creation and accessing of list and apply different kinds of operations on them")
print("1.Program to create and access list")
print("2.Progrm to demonstrate various list operation")
print("3.Program to demonstrate the use of functions and methods")
print("4.program to demonstrate the use of inbuilt functions")


print("1.Program to create and access list")
list1=[57,64,74,76,80,82,85]
print(list1)

print("2.Progrm to demonstrate various list operation")
print("Add")
list1=[57,64,74,76,80,82,85]
list2=[5,6,7,6,8,2,8]
b=list1+list2
print(b)

print("Replicate")
list1=[57,64,74,76,80,82,85]
c=list1*4
print(c)

print("Slicing")
list1=[57,64,74,76,80,82,85]
t=list1[1:4]
print(t)

print("Updating a list")
list1=[57,64,74,76,80,82,85]
p=list1[4]=74
print(p)

print("Append")
list1=[57,64,74,76,80,82,85]
list1.append(100)
print(list1)

print("Delete")
list1=[57,64,74,76,80,82,85]
del list1[4]
print(list1)


print("3.Program to demonstrate the use of functions and methods")
print("Max")
list1=[57,64,74,76,80,82,85]
print(max(list1))

print("Min")
list1=[57,64,74,76,80,82,85]
print(min(list1))

print("len")
list1=[57,64,74,76,80,82,85]
print(len(list1))


print("compare")
a=[57,64,74,76,80,82,85]
b=[58,64,74,7,80,8,85]
print(cmp(a,b))

print("4.program to demonstrate the use of inbuilt functions")
print("index")
list1=[57,64,74,76,80,82,85]
u=list1.index(74)
print(u)

print("count")
list1=[57,64,74,76,74,82,74]
e=list1.count(74)
print(e)


print("pop and pop(index)")
list1=[57,64,74,76,80,82,85]
e=list1.pop()
print(e)

print("pop and pop(index)")
list1=[57,64,74,76,80,82,85]
e=list1.pop(4)
print(e)

print("insert")
list1=[57,64,74,76,80,82,85]
list1.insert(4,'A')
print(list1)

print("Extend")
list1=[57,64,74,76,80,82,85]
list2=[57,64,74,76,80]
list1.extend(list2)
print(list1)

print("reverse")
list1=[57,64,74,76,80,82,85]
list1.reverse()
print(list1)

print("remove")
list1=[57,64,74,76,80,82,85]
list1.remove(80)
print(list1)


print("Sort")
list1=[5,1,7,9,43,28,18]
list1.sort()
print(list1)

































