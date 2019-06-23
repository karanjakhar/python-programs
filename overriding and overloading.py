#Function Overriding
class a:
    def fun(self):
        print("Base Class")

class b(a):
    def fun(self):
        print("Derived class")

obj=b()
obj.fun()
#----------------------------------------
#Function Overloading
class c:
    def tool(self,a,b):
        self.a=int(input('Enter a: '));
        self.b=int(input('Enter b: '));
        result=self.a+self.b
        print(result)
        
class d(c):
    def tool(self,a,b,c):
        self.a=int(input('Enter a: '));
        self.b=int(input('Enter b: '));
        self.c=int(input('Enter c: '));
        result=self.a*self.b*self.c
        print(result)

obj=d()
obj.tool(a,b,c)

#-------------------------------------------
#Operator Overloading
class a:
    def __init__(self,a):
        self.a=a
    def __add__(self,o):
        return self.a+o.a
    def __mul__(self,o):
        return self.a*o.a
    def __sub__(self,o):
        return self.a-o.a
    def __truediv__(self,o):
        return self.a/o.a
    def __floordiv__(self,o):
        return self.a//o.a
    def __gt__(self,o):
        if(self.a>o.a):
            return True
        else:
            return False

ob1=a(1)
ob2=a(2)
print(ob1+ob2)
print(ob1*ob2)
print(ob1-ob2)
print(ob1/ob2)
print(ob1//ob2)
print(ob1>ob2)
