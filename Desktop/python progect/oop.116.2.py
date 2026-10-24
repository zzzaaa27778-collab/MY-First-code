from abc import ABC,abstractmethod
class  BaseMeta(ABC):
     @abstractmethod  
     def o_oop(self):
       pass
class rr(BaseMeta) :
    def o_oop(self):
        return "fuck"
class ee(BaseMeta)           :
    def o_oop(self): 
        return "true"
class dss(BaseMeta) :
     def o_oop(self):
         return "Yes"      
class yyy(BaseMeta) :
     def o_oop(self):
         return "No" 
obj1=rr()
print(obj1.o_oop())    
obj2=ee()     
print(obj2.o_oop())