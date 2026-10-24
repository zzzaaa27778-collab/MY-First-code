def myD(func) :
    def ggfunc():
        print("Before")
        func()
        print("After")
    return ggfunc   
def say_Hello():
    print("Hello in my grande plan")
www=myD(say_Hello)    
www()
print("$"*10)
@myD
def dd():
     print("Hello in my grande plan")
dd()     
#@myD
#def ff():
#    print("Hello from my world")     
#dd()
#print("$"*10)    
#ff()