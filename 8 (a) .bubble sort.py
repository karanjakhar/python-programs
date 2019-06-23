list=[]
n=int(input('Enter the total number of elements : '))
x=0
for i in range(0,n):
    print('Enter the item number : ',i+1)
    x=int(input('Enter item : '))
    list.append(x)
print(list)
temp=0
for k in range(0,len(list)-1):
    for i in range(0,len(list)-(k+1)):
            if(list[i]>list[i+1]):
                temp=list[i]
                list[i]=list[i+1]
                list[i+1]=temp
print('SORTED LIST IS : ',list)
