a=[]
n=int(input('Enter the total number of elements : '))
x=0
for i in range(0,n):
    print('Enter the item number : ',i+1)
    x=int(input('Enter item : '))
    a.append(x)
print(a)

temp=0
for k in range(0,len(a)-1):
    for i in range(0,len(a)-(k+1)):
            if(a[i]>a[i+1]):
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
print(a)

