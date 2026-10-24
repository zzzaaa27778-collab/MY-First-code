marketweb=[]#الخطوة الاولى كتابة المعلومات
fulltry=10
try_n=1
while try_n <= fulltry :#الخطوة الثانية كتابة التكرار مع المتغيرات والدالات مثل ابيند  
        web=(input(f"Enter your web {try_n}"))
        marketweb.append(web)
        print(f"You have {try_n} tries used")
        try_n+=1
        print("Your websites list now :",marketweb)    
print("Your tries is finsh,Thanks for every thing ")# كتابة الكلمات النهائية خارج كتلة التكرار
print(f"Thats your web in marketweb list",marketweb)
6