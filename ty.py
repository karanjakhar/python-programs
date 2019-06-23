
print("1.Program to find whether a number is Even or Odd using function")
def number():
    x=int(input("Enter the Number : "))
    if(x%2==0):
        print("Even Number")
    else:
        print("odd Number")
number()

print("2.Program to Display calculator using function") 
def cal():
    print("1. Add 2.Sub 3.Mul 4.Div ")
    n=int(input("Enter the choice : "))
    if(n==1):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a+b
        print("Sum is : ",c)
    elif(n==2):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a-b
        print("Subtraction is : ",c)
    elif(n==3):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a*b
        print("Product is : ",c)
    elif(n==4):
        a=int(input("Enter the Number :"))
        b=int(input("Enter the Number :"))
        c=a/b
        print("Division is : ",c)
    else:
        print("invalid choice")
cal()        

print("3.Program to swap two numbers using function")
def swap():
    a=int(input("Enter the first Number: "))
    b=int(input("Enter the Second Number: "))
    c=a
    a=b
    b=c
    print("FIRST NUMBER: ",a)
    print("SECOND NUMBER: ",b)
swap()

print("4.Program to find fibonacci of number using function")
def fibbo():
    a=int(input("Enter the First Number of series-  "))
    b=int(input("Enter the Second Number of series-  "))
    n=int(input("Enter the Number of Terms needed-  "))
    print(a,b,end ="  ")
    while(n-2):
        c=a+b
        a=b
        b=c
        print(c,end="  ")
        n-=1
fibbo()

print()
print("5.Program to find Palindrome of number using function")
def palin(a):
    c=a;
    s=0;
    d=0;
    while(a!=0):
        d=a%10;
        s=(s*10)+d;
        a=a/10;
        a=int(a);

    if(c==s):
            print("Palindrome");
    else:
            print("Not palindrome")
a=int(input("Enter the Number: "))
palin(a);



























     
