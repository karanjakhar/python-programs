l= int(input("Enter the lenght of list: "))
print("Enter the keys: ")
k=[]
v=[]
d={}
for i in range(l):
    x=int(input())
    k.append(x)
print("Enter the values: ")
for i in range(l):
    y=input()
    v.append(y)
for i in range(l):
    d[k[i]]=v[k[i]-1]
print("The output of the following list into dictionary are: ")
print(d)
