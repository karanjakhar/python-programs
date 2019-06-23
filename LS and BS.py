print("SEARCHINGGGG")
arr=[]
n=int(input('Enter the number of terms in the list : '))
z=0
for i in range(0,n):
  print('Enter the item number : ',i+1)
  z=int(input('item : '))
  arr.append(z)
print("given array is : ",arr)

print("linear search result is : ")
x=int(input("the value to be searched : "))
for i in range(0,n):
  if(arr[i]==x):
    print('the entered number is present on position :',i+1)


print("binary search result is : ")
beg=0
end=len(arr)-1
loc=0
mid=int((beg+end)/2)
while(beg<=end and x!=arr[mid]):
  if(x<arr[mid]):
    end=mid-1
  else:
    beg=mid+1
  mid=int((beg+end)/2)

if(x==arr[mid]):
  loc=mid
  print("index of the element is :",loc)
else:
  loc=0
  print("Number doesn't Exist !")




