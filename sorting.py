print("BUBBLE SORT")
list=[]
n=int(input('Enter the total number of elements : '))
x=0
for i in range(0,n):
    print('Enter the item number : ',i+1)
    x=int(input('Enter item : '))
    list.append(x)
print(list)

# Bubble sort
for i in range(n):
    for j in range(n-i-1):
        if list[j]>list[j+1]:
            t=list[j]
            list[j]=list[j+1]
            list[j+1]=t
list

# Selection sort
for i in range(0,n-1):
    min=list[i]
    p=i
    for j in range(i+1,n):
        if list[j]<min:
            min=list[j]
            p=j
    if p!=i:
        t=list[i]
        list[i]=list[p]
        list[p]=t
list

# Insertion sort
list=[]
n= int(input("Enter the length of the list: "))
print("Enter the elements of an list")
for i in range(n):
    list.append(input())
for i in range (n):
    t=list[i]
    j=i-1
    while t<list[j] and j>=0:
        list[j+1]=list[j]
        j=j-1
    list[j+1]=t
list


def merge(arr, l, m, r): 
    n1 = m - l + 1
    n2 = r- m 
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = arr[l + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[m + 1 + j] 
    i = 0     
    j = 0     
    k = l     
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1
def mergeSort(arr,l,r): 
    if l < r: 
        m = int((l+(r-1))/2)
        mergeSort(arr, l, m) 
        mergeSort(arr, m+1, r) 
        merge(arr, l, m, r) 
arr=[]
n= int(input("Enter the length of the list: "))
print("Enter the elements of an list")
for i in range(n):
    arr.append(input())
mergeSort(arr,0,n-1)
print("Sorted list is: ")
print(arr)


