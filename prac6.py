
print('i).Program to enclosure different items in key-value pair')
A1={'Akshay':'7417269008','Sandeep':'7542735472','Ashutosh':'9866238463'}
A2={'Abc':'8763','BCD':'8797','RTW':'98080'}
print(A1)
print(A2)
print()
print('ii).Program to access dictionary by their keys')
print(A1['Akshay'])
print(A2['RTW'])
print()
print('iii).Program to update key-value pairs')
A1['Akshay']='8727970446'
A2['BCD']='8908'
print(A1)
print(A2)
print()
print('iv).Program to delete key-value in dictionaries')
del A2['RTW']
print(A2)
print()
print('v).Program to demonstrate in-build functions in dictionaries')
print('len()')
print(len(A1))
print()
print('keys()')
print(A1.keys())
print()
print('values()')
print(A1.values())
print()
print('items()')
print(A1.items())
print()
print('update()')
A1.update(A2)
print(A1)
print()
print('clear()')
A2.clear()
print(A2)
print()
print('copy()')
c=A1.copy()
print(c)
print()
print('getkey()')
print(A1.get('Akshay'))
print()
print('fromkeys()')
seq=('A','B','C')
A3={}
A3=A3.fromkeys(seq,100)
print(A3)


















