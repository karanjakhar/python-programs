n=int(input('number of prime numbers  you want : '))
c=0
for num in range(1,n+1):
    for i in range(1,num+1):
        if num%i==0:
            c=c+1
    if c==2:
        print(num)
    c=0
