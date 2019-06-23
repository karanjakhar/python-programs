#Program to enclose different items in key-value pair
A1={'NAME':'SANDEEP','PHONE':8687950793,'UID':'17BCS2782'}
A2={'NAME':'SANDY','PHONE':7417269008,'UID':'17BCS2774'}
A3={'NAME':'ASHUTOSH','PHONE':7080990648,'UID':'17BCS2782'}
print(A1)

print()
print()
print()

#Program to access dictionary by their keys
print(A2['NAME'])
print(A3['UID'])

print()
print()
print()

#Program to update key-value pairs
A1['NAME']='SANDEEP THAKUR'
A2['PHONE']=9140930748
print(A1)
print(A2)

print()
print()
print()

#Program to delete key-value in dictionaries
print('del() function : deleting name of dictionary A2')
del A2['NAME']
print(A2)

print()
print()
print()

#Program to demonstrate in-build functions in dictionaries
print('len() function : ',len(A1))
print('keys() function : ',A1.keys())
print('values() function : ',A1.values())
print('items() functions : ',A1.items())
A5={'NA':'SANDEEP','PHO':8687950793,'ID':'17BCS2782'}
A1.update(A5)
print('by using update() function : ',A1)
A2.clear()
print('by using clear() function : ',A2)
c=A1.copy()
print('copy of A1 dictionary using copy() function : ',c)
print('get() function : ',A1.get('NAME'))
print('fromkeys() function : ')
seq=('A','B','C')
A3={}
A3=A3.fromkeys(seq,100)
print(A3)


















