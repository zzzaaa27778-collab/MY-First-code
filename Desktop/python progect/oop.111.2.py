class data1:
    def __init__(self):
       print("data1")
       pass
class data2 :
    def __init__(self):
     print("farc v2")    
     pass
class aizen(data1,data2):
     def __init__(self):
        super().__init__()
        pass  
hhh=aizen() 
print(aizen.mro())     
       

