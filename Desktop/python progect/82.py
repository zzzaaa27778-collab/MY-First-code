
def ff():
    yield 1
    yield 2
    yield 3
    yield 4
    print(ff())
for number in ff():
    print(number)
print()
my_Pf=ff()    
print(next(my_Pf))
print("hhhd[wv[nkv[nae]]]")
print(next(my_Pf))
print("hhhd[wv[nkv[nae]]]")
print(next(my_Pf))
print("hhhd[wv[nkv[nae]]]")
print(next(my_Pf))
print("hhhd[wv[nkv[nae]]]")
for number in my_Pf:
    print(number)