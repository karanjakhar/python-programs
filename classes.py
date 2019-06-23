class a:
    def sum(self):
        self.a=int(input('enter a : '))
        self.b=int(input('enter b : '))
        result=self.a+self.b
        print('sum ',result)
obj=a()
#simple class
#obj.sum()

class b(a):
    def mul(self):
        self.a=int(input('enter a : '))
        self.b=int(input('enter b : '))
        result=self.a*self.b
        print('mul ',result)
        
obj1=b()
#single level
#obj1.sum()
#obj1.mul()

class e(b):
    def sqr(self):
        self.a=int(input('enter number for square : '))
        result=self.a*self.a
        print('square ',result)
#multi level
obj4=e()
#obj4.sum()
#obj4.mul()
#obj4.sqr()


class c:
    def div(self):
        self.a=int(input('enter divident : '))
        self.b=int(input('enter divisor : '))
        result=self.a/self.b
        print('div ',result)

class d(a,c):
    def sub(self):
        self.a=int(input('enter a : '))
        self.b=int(input('enter b : '))
        result=self.a-self.b
        print('sub ',result)

obj3=d()
#multiple base
#obj3.sum()
#obj3.sub()

class f(a):
    def cube(self):
        self.a=int(input('enter number for cube : '))
        result=self.a*self.a*self.a
        print('cube is ',result)

obj5=f()
#obj5.sum()
#obj1.sum()

class h(d):
    def quad(self):
        self.a=int(input('enter number for quad multiply : '))
        result=self.a*self.a*self.a*self.a
        print('quadruple multiple  is ',result)
obj6=h()
obj6.quad()
obj6.sub()
obj6.sum()
obj6.div()
