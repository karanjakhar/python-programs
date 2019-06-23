#==========================================================================

#===============================

a = int(input("Enter first number: "))
b= int(input("Enter second number: "))
c= int(input("Enter third number: "))
 
if (a > b) and (a > c):
   largest = a
elif (b > a) and (b > c):
   largest =b
else:
   largest = c
 
print("The largest number is",largest)
#===================================================================
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
        
    return x

a = [2, 4, 6, 8, 16] 
  
num1 = a[0] 
num2 = a[1] 
gcd = find_gcd(num1, num2) 
  
for i in range(2, len(a)): 
    gcd = find_gcd(gcd, a[i]) 
print("GCD OF THE NO IS :")     
print(gcd) 

#=============================================================

x=int(input("Enter upper limit: "))
for a in range(2,x+1):
    x=0
    for i in range(2,a//2+1):
        if(a%i==0):
            x=x+1
 
    if(x<=0):
        print(a)
#==================================================================
def newtonSqrt(n,h):
    approx = 0.5 * n
    for i in range(h):
        betterapprox = 0.5 * (approx + n/approx)
        approx = betterapprox
    return betterapprox

print(newtonSqrt(10, 3))
print(newtonSqrt(10, 5))
print(newtonSqrt(10, 10))

#=====================================================================
n=int(input("Enter a number "))
sum = 0
i= 1

while i <= n:
    sum = sum + i
    i = i+1
    
print("The sum of first",n)
print("natural number is ",sum)
#================================================================
nterms = int(input("How many terms? "))
n1 = 0
n2 = 1
c = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while c < nterms:
       print(n1,end=',')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       c= c+1
#====================================================================
# Python program to find the factorial of a number provided by the user.
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
#========================================================================
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))

n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
#========================================================================
def factorial(x):
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result
print (factorial(10))

#========================================================================
n_num = [1, 2, 3, 4, 5] 
n = len(n_num) 
  
get_sum = sum(n_num) 
mean = get_sum / n 
  
print("Mean / Average is: " + str(mean))
#-----------
n_num = [1, 2, 3, 4, 5] 
n = len(n_num) 
n_num.sort() 
  
if n % 2 == 0: 
    median1 = n_num[n//2] 
    median2 = n_num[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = n_num[n//2] 
print("Median is: " + str(median)) 
