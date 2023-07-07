fh = open("data.txt")
print(type(fh)) # <class '_io.TextIOWrapper'>
print(fh) # <_io.TextIOWrapper name='data.txt' mode='r' encoding='cp1251'>
print(fh.read(3)) # 'Hel'
print(fh.tell())#3
print(fh.seek(0)) #0
print(fh.readline()) # 'Hello world\n'
print(fh.readline()) # 'Python is amazing\n'
print(fh.seek(0)) #0
print(fh.readlines()) # ['Hello world\n', 'Python is amazing\n']
print(fh.closed) # False
fh.close()
print(fh.closed) # True
#print(fh.readlines()) # ValueError: I/O operation on closed file.
