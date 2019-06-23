#Program to demonstrate the use of Various string function
ab='sAndeep'
cd='singh'
ef='e'
gh='p'
print("capitalize function :",ab.capitalize())
print("count function :",ab.count('ee'))
print("endswith function :", ab.endswith('p'))
print("startswith function :",cd.startswith('s'))
print("islower function :",ab.islower())
print("isupper function :",ab.isupper())
print("lower function :",ab.lower())
print("upper function :",ab.upper())
abcd='hello'
print("find function :",abcd.find('x'))
print("index function :",abcd.index('l'))
print("swapcase function :",ab.swapcase())
abc='    hello123       '
print("lstrip function :",abc.lstrip())
print("rstrip function :",abc.rstrip())
print("isdigit function :",ab.isdigit())
print("isalpha function :",ab.isalpha())
print("isalnum function :",ab.isalnum())
print("len function :",len(ab))
#Program to demonstrate the use of concatenation
a='sandeep '
b='singh'
print("concatination is : ",a+b)
      
#Program to retrieve string in normal and reverse order
e='android development'
print("normal order : ",e)
print("reverse order : ",e[::-1])

#Program to demonstrate the use of replication operation
print("replication is : ",3*a)

#Program to demonstrate the use of membership operator (IN and NOT IN)
t=a not in b
print("a NOT IN b : ",t)
t=a in b
print("a IN b : ",t)

#Program to demonstrate the use of relational operator
xyz='a'
abc='b'
y=xyz>abc
u=xyz<abc
print("relational operator > : ",y)
print("relational operator < : ",u)

#Program to demonstrate the use of Slice notation
e='android development'
print("syntax of slicing is  [start:stop:steps] :")
print("here e='android development'")
print("e[::-1] : ",e[::-1])
print("e[:2] : ",e[:2])
print("e[2:] : ",e[2:])
print("e[0] : ",e[0])
print("e[::+2] : ",e[::+2])
print("e[3:9] : ",e[3:9])
print("e[-1:-12:-2] : ",e[-1:-12:-2])


     
