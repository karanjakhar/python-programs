#N prime NUmber
c=0
n=int(input("Enter n: "))
for num in range(1,n+1):
    for i in range(1,num+1):
        if(num % i)==0:
            c=c+1
    if c==2:
        print(num)
    c=0
#-----------------------------------
    
