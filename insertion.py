a=[]
n=int(input('Enter the number of elements : '))
x=0
for i in range(0,n):
    print('Enter the item number : ',i+1)
    x=int(input('Enter item : '))
    a.append(x)
print(a)

for k in range(1,len(a)):
    temp= a[k]
    i=k-1
    while((temp<a[i]) and (i>=0)):
        a[i+1]=a[i]
        i-=1
        a[i+1]=temp
print(a)
