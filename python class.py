#classs
class a:
    def root(self):
        print("Welcome to Chandigarh University");
obj=a()
obj.root();
#inheritance
#single
class abc:
    def sum(self):
        self.a=10;
        self.b=20;
        result=self.a+self.b
        print(result);
    

class xyz(abc):
    def mul(self):
        self.p=10;
        self.q=12;
        result=self.p*self.q
        print(result);

obj1=xyz()
obj1.mul()
obj1.sum()

#single with user input
class abc:
    def sum(self):
        self.a=int(input('Enter a: '))
        self.b=int(input('Enter b: '))
        result=self.a+self.b
        print(result);
    

class xyz(abc):
    def mul(self):
        self.p=int(input('Enter p: '))
        self.q=int(input('Enter q: '))
        result=self.p*self.q
        print(result);

obj1=xyz()
obj1.mul()
obj1.sum()


#Multiple

class abc:
    def sum(self):
        self.a=10;
        self.b=20;
        result=self.a+self.b
        print(result);
    

class xyz:
    def mul(self):
        self.p=10;
        self.q=12;
        result=self.p*self.q
        print(result);

class r(abc,xyz):
    def display(self):
        print("Hello");
        
obj1=r()
obj1.display()
obj1.mul()
obj1.sum()

#Multilevel

class abc:
    def sum(self):
        self.a=10;
        self.b=20;
        result=self.a+self.b
        print(result);
    

class xyz(abc):
    def mul(self):
        self.p=10;
        self.q=12;
        result=self.p*self.q
        print(result);

class r(xyz):
    def display(self):
        print("Hello");
        
obj1=r()
obj1.display()
obj1.mul()
obj1.sum()

#Hierarchical
class abc:
    def sum(self):
        self.a=10;
        self.b=20;
        result=self.a+self.b
        print(result);
    

class xyz(abc):
    def mul(self):
        self.p=10;
        self.q=12;
        result=self.p*self.q
        print(result);


class r(abc):
    def display(self):
        print("Hello");
        
obj1=r()
obj2=xyz()
obj1.display()
obj2.mul()
obj1.sum()
obj2.sum()


#Hybrid

class abc:
    def sum(self):
        self.a=10;
        self.b=20;
        result=self.a+self.b
        print(result);
    

class xyz:
    def mul(self):
        self.p=10;
        self.q=12;
        result=self.p*self.q
        print(result);

class r(abc,xyz):
    def display(self):
        print("Hello");

class d(r):
    def tool(self):
        print("Hybrid");
obj=d()
obj.tool()
obj1=r()
obj1.display()
obj1.mul()
obj1.sum()















