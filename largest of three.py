a=int(input('enter a :'))
b=int(input('enter a :'))
c=int(input('enter a :'))
def largest_num(x,y,z):
    if x>y and x>z:
        print(x)
    elif y>x and y>z:
        print(y)
    else:
        print(z)
print('largest :',end="")
largest_num(a,b,c)