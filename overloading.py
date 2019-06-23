class a:
    def sum(self):
        print('1st  function ')

    def sum(self,a,b):
        self.a=a
        self.b=b
        result=self.a+self.b
        print('sum ',result)
obj=a()
obj.sum()
obj.sum(100,50)
