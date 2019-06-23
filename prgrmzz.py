Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
c=0
n=int(input("Enter n"))
for i in range(2,n+1):
    for k in range(1,i+1):
        if(i % k)==0:
            c=c+1
        if c==2:
            print(i)
        c=0
            
    
        
            
        
    












