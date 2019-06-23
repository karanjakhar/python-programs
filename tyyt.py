print("Sum of items in list")
list1=[12,45,78,76,70,66]
sum=0
for i in range(0,5):
    sum+=list1[i]
print(sum)

print("Multiplication of items in the list")
mul=1
for i in range(0,5):
    mul+=list1[i]
print(mul)

print("Copying the list")
a=list1
k=list1.copy()
s=list1[0:6]
print(a)
print(k)
print(s)


