x=[1,2,3,4,5,6,7,8,9,10]
def y(x):
    return x %2==0
z=list(filter(y,x))
print(z)
z=list(filter(lambda x:x %2==0,x))    
print(z)