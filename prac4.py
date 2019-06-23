print("Program to demonstrate various kinds of operations that are applied on string")

print("1. Program to demonstrate the use of concatenation")
str1='Chandigarh '
str2='University'
con=str1+str2
print(con)
      
print("2. Program to retrieve string in normal and reverse order")
str3='Akshay'
print(str3)
c=str3[::-1]
print(c)

print("3. Program to demonstrate the use of replication operation")
str4=' Akshay '
d=4*str4
print(d)

print("4. Program to demonstrate the use of membership operator (IN and NOT IN)")
str5='Chandigarh'
str6='university'
t=str6 not in str5
print(t)

str5='Chandigarh'
str6='university'
t=str6 in str5
print(t)

print("5. Program to demonstrate the use of relational operator")
str7='Akshay'
str8='Akshayy'
y=str7>str8
u=str7<str8
print(y)
print(u)

print("6. Program to demonstrate the use of Slice notation")
str9='Chandigarh University'
print(str9)
o=str9[3:9]
print(o)

str9='Chandigarh University'
print(str9)
o=str9[7:9]
print(o)

str9='Chandigarh University'
print(str9)
o=str9[:5]
print(o)

str9='Chandigarh University'
print(str9)
o=str9[3:]
print(o)

print('New program')
str10='Akshay'
print(str10)
p=str10[-1:-5:-4]
print(p)
print()

print("7. Program to demonstrate the use of Various string function")


strr='akshay Jawla'
i=strr.capitalize()
print(i)


strr='akshay'
strrr='a'
i=strr.count(strrr)
print(i)


strr='akshay'
strrr='y'
i=strr.endswith(strrr)
print(i)

strr='akshay'
strrr='y'
i=strr.startswith(strrr)
print(i)

strr='akshay jawla'
i=strr.islower()
print(i)

strr='AKSHAY JAWLA'
i=strr.isupper()
print(i)


strr='AKSHAY JAWLA'
i=strr.lower()
print(i)

strr='akshay jawla'
i=strr.upper()
print(i)

strr='akshay'
strrr='y'
i=strr.find(strrr)
print(i)

strr='akshay'
strrr='k'
i=strr.index(strrr)
print(i)

strr='akshay'
i=strr.index('a',4,5)
print(i)


strr='AksHay jAwLa'
i=strr.swapcase()
print(i)


strr='   akshay'
i=strr.lstrip()
print(i)

strr='akshay   '
i=strr.rstrip()
print(i)


strr='Akshay2774'
i=strr.isdigit()
print(i)

strr='Akshay2774'
i=strr.isalpha()
print(i)

strr='Akshay2774'
i=strr.isalnum()
print(i)

strr='AkshayJawla'
i=len(strr)
print(i)







