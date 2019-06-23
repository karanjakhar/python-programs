list=[]
n=int(input('Enter the number of terms in the list : '))
z=0
for i in range(0,n):
  print('Enter the item number : ',i+1)
  z=int(input('item : '))
  list.append(z)
print("given array is : ",list)
x=int(input("the value to be searched : "))
beg=0
end=len(list)-1
loc=0
mid=int((beg+end)/2)
while(beg<=end and x!=list[mid]):
  if(x<list[mid]):
    end=mid-1
  else:
    beg=mid+1
  mid=int((beg+end)/2)

if(x==list[mid]):
  loc=mid
  print("index of the element is :",loc)
else:
  loc=0
  print("Number doesn't Exist !")



for i in range(0,n):
  if(list[i]==x):
    #print('the entered number is present on position :',i+1)
    break;
