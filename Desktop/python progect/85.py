def qq(ffff):
    def ww(*numbers):
        for number in numbers :
            if number < 0 :
                print("The number is zero")
        return ffff(*numbers)
    return ww
@qq
def cc(*numbers) :       
    print(sum(numbers))
print("-----التجربة الاولى (ارقام موجبة)-----")  
cc()  
print("-----التجربة الثانية  (ارقام سالبة)-----")  
cc()


from time import time 
def gg(func):
   def wrapper(*args,**kwargs):
       start_time=time()
       result=func(*args,**kwargs)
       end_time=time()
       print(f"\n[Time taken]:{end_time-start_time}seconds")
       return result
   return wrapper
@gg
def safd(p):
    for i in range(1, p +1):
        print(i)
    print() 
print("بدء عملية العد حتى 200---")    
safd(10000)   
#def jj(u1,u2):
 #   def yy(x,y):return 
#print(jj(1,200))
#jj()       
   