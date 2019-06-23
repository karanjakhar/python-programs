f=open('sample.txt','w')
string1=input('Enter text for sample.txt to write : ')
f.write(string1)
print('file sample.txt is written')
f.close()
#opening a file in read mode
f=open('sample.txt','r')
print('content of sample.txt is ',f.read())
f.close()
#opening a file in append mode
f=open('sample.txt','a')
string1=input('Enter text for sample.txt to be appended : ')
f.write(string1)
print('file sample.txt appended')
f.close()
#opening a file in read mode
f=open('sample.txt','r')
print('content of sample1.txt after apending is ',f.read())
f.close()
#opening another file in write mode
f=open('sample1.txt','w')
f.write('i am Akshay Jawla uid 17bcs2774')
f.close()
#opening another file in read and write mode
f=open('sample1.txt','r+')
print('content of file2 is : ',f.read())
string2=input('Enter text for sample1.txt to write : ')
f.write(string2)
f.close()
#reading it again through read mode
f=open('sample1.txt','r')
print('content of file1 is : ',f.read())
f.close()
#demonstration of readline function()
f=open('sample1.txt','r')
print('readline() is : ',f.readline())
print('readline(4) is : ',f.readline(4))
f.close()
# x mode for exclusive creation of file
f=open('sample69s.txt','x')
f.write('Akshay')
f.close()
f=open('sample69s.txt','r')
print('Empty file created through x mode')
f.close()
#removing the exixting file by using remove function of imported package os
import os
os.remove("jawla.txt")
print("jawla.txt File Removed!")

