class x():
    def oop(self):
        print("Hello Itachi my ligend")
class c(x):
    def oop(self):
        print("BMW")
        super().oop()        
class v(x)   :
    def oop(self):
        super().oop()
        print("The oop is harder than Basic Brogramming") 
print("_______bbbbb_xx________")    
object_jjj= x() 
object_jjj.oop()
print("________\n_________cc_-----------")
object_r=c()
object_r.oop()
print("_\n_________vvvv________-----")
object_e=v()
object_e.oop()
print("\n_----blblblblaaaa---")
object_list=[x(),c(),v()]
for obj in object_list :
    obj.oop()