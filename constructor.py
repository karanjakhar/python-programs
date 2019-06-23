class a:
    a=0
    b=0
    def __init__(self):
        a.a=15
        a.b=10
    def display(self):
        print('a : ',a.a)
        print('b : ',a.b)
obj=a()
obj.display()

class b:
    def __init__(self,id,name):
        self.id=id
        self.name='sandeep'
    def display(self):
        print('id  : ',self.id)
        print('name  : ',self.name)
obj1=b(1,'sandeep')
obj1.display()