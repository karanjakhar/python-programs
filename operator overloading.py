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
ob1 = a(10) 
ob2 = a(7)   
print(ob1+ob2)
print(ob1*ob2) 
print(ob1-ob2)
print(ob1/ob2) 
print(ob1//ob2)
print(ob1>ob2)  
