list=[]
n=int(input('Enter the total number of elements : '))
x=0
for i in range(0,n):
    print('Enter the item number : ',i+1)
    x=int(input('Enter item : '))
    list.append(x)
print(list)
for k in range(1,len(list)):
    temp=list[k]
    i=k-1
    while((temp<list[i]) and (i>=0)):
        list[i+1]=list[i]
        i-=1
        list[i+1]=temp
print('SORTED LIST IS : ',list)
