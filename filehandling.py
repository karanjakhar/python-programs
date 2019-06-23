f=open('sample.txt','w')
f.close()
#------------------------------
f=open('sample.txt','w')
string1=input()
f.write(string1)
f.close()
#----------------------------------
f=open('sample.txt','r')
print('content of file1 is ',f.read())
f.close()
#-------------------------------------
f=open('sample.txt','a')
string1=input('Enter text for sample.txt to be appended : ')
f.write(string1)
f.close()
#---------------------------------------
f=open('sample.txt','r')
print('content of file1 after apending is ',f.read())
f.close()
#--------------------------------------------------------
f=open('sample1.txt','w')
f.write('I am Akshay UID- 17BCS2774')
f.close()
f=open('sample1.txt','r+')
print('content of file2 is : ',f.read())
string2=input()
f.write(string2)
f.close()
#---------------------------------------
f=open('sample1.txt','r')
print('content of file1 is : ',f.read())
f.close()
#--------------------------------------
f=open('sample3.txt','w')
f.write('HEllo welcome to CU')
f.close()
f=open('sample3.txt','r')
print('readline is : ',f.readline())
print('readline is : ',f.readline(4))
f.close()
#----------------------------------------
f=open('sample76.txt','x')
f.write('Akshaay')
f.close()
f=open('sample76.txt','r')
print('x mode : ',f.read())
f.close()
#----------------------------------------
import os
os.remove("jawla.txt")
print("File Removed!")
