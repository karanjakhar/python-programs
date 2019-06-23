print("programs to Demonstrate the use of Function and passing Different types of arguments")

print("1.Program to Demonstrate the use of function")
def mike():
    print("HEllo")
    print("CHANDIGARH UNIVERSITY")
mike()
    
print("Program to Demonstrate the use of Return Statement")
def hike():
    x=int(input("Enter the value of x -"))
    y=int(input("Enter the value of y -"))
    z=x+y
    return (z)
u= hike()
print(u)

    
print("Program to Demonstrate the use of Passing arguments to functions"
def sum(b,a):
    print(b,a)
    return(b+a);
t=sum(9,8)
print(t)

print("Program to Demonstrate the use of Passing default arguments")
def default(x=10,y=41):
    print(x+y)
default()

print("Program to Demonstrate the use of Passing keyword arguments")
def keyword(id="17BCS2774"):
    print("keyword function")
    print(id)
keyword()

print("Program to Demonstrate the use of Scope function")
a=20
def scope():
    b=13
    c=a+b
    print("scope function calling")
    print(c)
scope()



    
