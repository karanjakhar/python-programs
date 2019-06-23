n=int(input('size of square matrix'))
a=[[None]*n for i in range(n)]
b=[[None]*n for i in range(n)]
c=[[None]*n for i in range(n)]
d=[[None]*n for i in range(n)]
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=int(input())
print(a)
for i in range(0,n):
    for j in range(0,n):
        b[i][j]=int(input())
print(b)
for i in range(0,n):
    for j in range(0,n):
        c[i][j]=a[i][j]+b[i][j]
print('add : ',c)
for i in range(0,n):
    for j in range(0,n):
        d[i][j]=0
        
for i in range(0,n):
    for j in range(0,n):
        for k in range(0,n):
            d[i][j]+=a[i][k]*b[k][j]
print('mul : ',d)
