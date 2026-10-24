def qq(ffff):
    def ww(x,y):
        if x<0 or y<0 :
            print("You have one number wrong!!!")
        return ffff(x,y)
    return ww
@qq
def cc(x,y):
    print(x+y)
print("-----التجربة الاولى (ارقام موجبة)-----")  
cc(100,900)  
print("-----التجربة الثانية  (ارقام سالبة)-----")  
cc(-150,60)
  #      print("Start")
   #     result=x+y
    #    print(result)
     #   print("Finish")
      #  return result
#    return ww(n1,n2)
#print(qq(10,20))
#        ww(n1+n2)
 #       print("Finish")
  #      ww(10,20) 
#print(qq())              
#print(ww())              