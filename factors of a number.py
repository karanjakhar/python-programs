num=int(input('enter number :'))
def factor(n):
    i=2
    while(n!=1):
        if n%i==0:
            print(i)
            n=int(n/i)
            i=2
        else:
            i=i+1
factor(num)