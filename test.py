name="yahya"
age=18
country="palistine"
print(f"My name is {name} and the age is {age:.2f} also i love my {country}")
print(f"My name is {name} and the age is {age*5} also i love my {country}")
print(f"My name is {name} and the age is {age+10} also i love my {country}")

TEXT1=-6
TEXT2=10.99
TEXT3="3+5J"
print(type(4))
print(type(10.9))
print(type(3+5j))

print(2+3)
print(6-3)
print(5*7)
print(15//5)
print(2*3+5//5)
print((7+8)*5+7//7)

print(10//3)
print(7**2)
print(3**2*3+4)
print(10%3)
print(16.6/5)
print(f"{16.6/5:.3f}")
print(f"{45.3*9+6.:7f}")
TEXT1=['one','TOW','sam',False,'5j','K+']

print(TEXT1[0:5])
print(TEXT1[0:3]) 
print(TEXT1[0:3:4]) 
print(TEXT1[0],TEXT1[4],TEXT1[2]) 
print(TEXT1[0:4:3]) 
TEXT1[1]=2 
print(TEXT1[1])
print(TEXT1)

TEXT1=["one",2,'sam','5j',False]
TEXT2=3,4,5
TEXT1.append(TEXT2)
print(TEXT1)
print(TEXT2)
TEXT1.append(2)
print(TEXT1)
TEXT1.append('jak')
TEXT1.append('5x')
TEXT1.append(25)
print(TEXT1)
TEXT1.append([1,2,3,5])
print(TEXT1)
print()


a=[1,2,'s','5j','Qa',2,2]
b=[67,'rtx',000]
a.extend(b)
print(a)
a.remove(2)
print(a)
print()
a=[1,-5,6,88,-55,0]
a.reverse()
print(a)
a.sort(reverse= False)
a.sort(reverse= True)
print(a)
x=[1,-5,6,88,-55,0,'yahya']

x.reverse()
print(x)
a=[1,2,3,5]
a.clear()
print(a)
print()

f=[1,-5,6,88,-55,0,'yahya']

b= f.copy()
b.append(9)
print(f)
print(b)
s=[1,6,7,9,8,6,6,6,6,6]
print( s.count(6)) 
print(s+f)
print(s.index(6))
print(s.index(1+6))
s.insert(3,'dh')
print(s)
s.insert(3,'dh')
print(s)
print(100==100)
print(100!=100)
print(100>=300)
print(100<=300)
print(100<300)
print(100>300)
Uname='Yahya'
Uage=18
Ucountry='palistine'
Book='a'
priceBook=100
if True:
    print(f"Hello my name is {Uname} and the age is {Uage} also the  is {Book} and the value is {priceBook} the last think I love my {Ucountry}")
if False:
      print(f"Hello my name is {Uname}  age is {Uage} also the book is {Book} and the  is {priceBook} the last think I love my {Ucountry}")     
if Uage== 19 and Uname=='Yahya':
        print("kakashi")
if Ucountry=='palistine' and priceBook==100 or Book==s:
        print(f"Hello my name is {Uname} and the age is {Uage} also the book is {Book} and the value is {priceBook} the last think I love my {Ucountry}")
elif Uage== 18 and Uname=='sami': 
         print("itatchi")
          
elif priceBook==100 and Ucountry=='palistine':
        print(f"Hello my name is {Uname} and the age is {Uage} also the  is {Book} and the value is {priceBook} the last think I love my {Ucountry}")
else:
        print(f"Hello my name is {Uname}  age is {Uage} also the book is {Book} and the  is {priceBook} the last think I love my {Ucountry}")

priceBook=50
Value=30
if priceBook > Value :
       print("You can not buy ") 
else :
         print("You can buy ") 
print("You can not buy ") if priceBook > Value else  print("You can buy ") 