zero=open("65.py.txt","r")
print(zero.name)
print(zero.encoding)
print(zero.mode)
print(zero.read())
print(zero.read(10))
print(zero.readlines())
print(tuple (zero.readlines()))
print(zero.readlines(5))
print(zero.readlines(5))
print(type (zero.readlines(5)))
print(zero.mode)
zero.seek(0)
for line in zero :
    print(line)
    if line.startswith("5") :
        print(line)
        break