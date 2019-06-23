num1=int(input('enter number 1  :'))
num2=int(input('enter number 2  :'))
def gcd(n1,n2):
    hcf=1
    if n1>n2:
        smaller=n2
    else:
        smaller=n1
    for i in range(1,smaller+1):
        if n1%i==0 and n2%i==0:
            hcf=i
    print('hcf or gcd is : ',hcf)
gcd(num1,num2)
