def febonacci(n):
    t1=0
    t2=1
    nextterm=0
    for i in range(0,n):
        print(t1,end="  ")
        nextterm=t1+t2
        t1=t2
        t2=nextterm
febonacci(15)
        
