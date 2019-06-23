list=[]
n=int(input('Enter the total number of elements : '))
x=0
for i in range(0,n):
    print('Enter the item number : ',i+1)
    x=int(input('Enter item : '))
    list.append(x)
print(list)
#-------------------------------------------------------------------
temp=0
for k in range(0,len(list)-1):
    min=list[k]
    pos=k
    for i in range(k+1,len(list)):
        if(min>list[i]):
            min=list[i]
            pos=i
    if(pos!=k):
        temp=list[k]
        list[k]=list[pos]
        list[pos]=temp
print(list)
