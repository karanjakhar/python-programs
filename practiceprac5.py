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
