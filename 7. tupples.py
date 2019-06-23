# creating a tupples
#empty tupple
s1=()
print('s1 : ',s1)
#tupple with multiple elements and accessing it
s2=(2782,'thakur',99)
print('s2 : ',s2)
#another way to create tupples and access them
S3=(82,85,96,56,70,99)
print('S3 : ',S3)
s4=74,'sandeep',90
print('s4 : ',s4)
s3=(82)
print('s3=(82): ',s3)
#creating new tupple and including previous tupple values in it
s5=s1,(27,'thakur')
print('s5=s1,(27,\'thakur\') : ',s5)
#1 slicing
print(S3[0])
print('s3[0] : ',S3[0])
print('s3[::-1] : ',S3[::-1])
print('s3[0:2] : ',S3[0:2])
#2 add i.e concatination
print('s3+s2 : ',S3+s2)
#3 replication
print('s3*5 : ',S3*5)
#some functions  of tupples
print('min(s3) : ',min(S3))
print('max(s3) : ',max(S3))
print('len(s3) : ',len(S3))

