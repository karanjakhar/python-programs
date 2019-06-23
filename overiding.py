class a:
    def sum(self):
        self.a=int(input('enter a : '))
        self.b=int(input('enter b : '))
        result=self.a+self.b
        print('sum ',result)

class b(a):
    def sum(self):
        self.a=int(input('enter a : '))
        self.b=int(input('enter b : '))
        result=self.a*self.b
        print('mul ',result)
        
obj=b()
obj.sum()
